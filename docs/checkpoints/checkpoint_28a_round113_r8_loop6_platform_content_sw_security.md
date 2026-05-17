# Checkpoint 28A Round 113: R8 Loop-6 Platform/Content/SW/Security

## 목적

`docs/round/round_113.md`의 R8 Loop-6 내용을 calibration/evaluation 자료로 반영했다. 이번 라운드는 플랫폼, 콘텐츠, SW, 보안 영역에서 `AI 기능`, `유저 수`, `신작 기대`, `광고 회복`, `보안 수요`를 실제 반복매출 증거와 분리하는 것이 핵심이다.

간단한 예시:

- `AI 기능 출시`는 Stage 1 관찰 신호다.
- `AI ARR`, `고객 attach`, `낮은 churn`, `gross margin 안정`, `FCF 전환`이 함께 확인되어야 더 높은 단계로 볼 수 있다.
- 보안 수요가 좋아도 대형 장애나 고객 소송이 있으면 Green 근거가 아니라 RedTeam 확인 대상이다.

## 반영 내용

- 신규 archetype 3개 추가:
  - `GOVERNMENT_AI_PROGRAM_OF_RECORD`
  - `LEGACY_SAAS_AI_REINFORCEMENT`
  - `CYBERSECURITY_AI_THREAT_DEMAND`
- Round 113 전용 모듈 추가:
  - `src/e2r/sector/round113_r8_loop6_platform_content_sw_security.py`
  - `src/e2r/cli/build_round113_r8_loop6_report.py`
- 테스트 추가:
  - `tests/test_round113_r8_loop6_platform_content_sw_security.py`
- 산출물 생성:
  - `data/e2r_case_library/cases_r8_loop6_round113.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round113_r8_loop6_v6.csv`
  - `output/e2r_round113_r8_loop6_platform_content_sw_security/`

## 결과 요약

- score targets: 27
- case candidates: 21
- structural_success: 1
- success_candidate: 8
- event_premium: 1
- Stage 4B/watch 포함 케이스: 8
- Stage 4C/thesis-break 케이스: 6
- Green possible target: 3
- Watch/Yellow-first target: 15
- RedTeam-first target: 9
- gate-only target: 7

## 핵심 분리

### Government AI

Palantir Q4 케이스를 `ENTERPRISE_AI_ONTOLOGY_WORKFLOW` 단독이 아니라 `GOVERNMENT_AI_PROGRAM_OF_RECORD` 중심으로 재분류했다. 정부 AI pilot이 실제 장기 예산과 program of record로 고정되는지 보는 축이다.

### Legacy SaaS AI

Salesforce Agentforce류 케이스를 `LEGACY_SAAS_AI_REINFORCEMENT`와 `LEGACY_SAAS_AI_DISRUPTION_OVERLAY`로 분리했다. AI agent가 ARR attach와 workflow lock-in을 강화하면 후보가 될 수 있지만, seat/license downsell이나 gross margin 훼손이면 RedTeam 축이다.

### Cybersecurity AI Threat Demand

Fortinet 케이스를 `CYBERSECURITY_AI_THREAT_DEMAND`로 분리했다. AI threat 자체가 아니라 billings, ARR, renewal, operational trust로 연결되는지를 확인한다.

### AI Networking / Edge AI Cloud

Akamai와 Cisco 케이스를 추가해 AI cloud revenue contribution, hyperscaler AI orders, restructuring cost, legacy networking mix를 별도 검증 필드로 두었다. 주문이나 계약이 있어도 margin, capex, FCF 전환이 없으면 Green으로 승격하지 않는다.

## Guardrails

- 이번 라운드는 production scoring을 바꾸지 않는다.
- case record는 candidate-generation input이 아니다.
- Stage 3-Green 기준은 완화하지 않았다.
- ARR, bookings, churn, FCF, customer damage, lawsuit, stage price는 확인된 증거 없이 만들지 않는다.
- 단일 IP 이벤트, 유저 수 증가, 광고 회복, 보안 수요, AI 기능 출시는 단독 Green 근거가 아니다.

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round113_r8_loop6_report
PYTHONPATH=src python -m unittest tests.test_round113_r8_loop6_platform_content_sw_security -v
```

## 다음 작업

Round 113 산출물은 R8 scoring 적용 전 calibration 자료다. 다음 라운드에서 가격 경로와 MFE/MAE를 채우고, 기존 score와 archetype-aware shadow score를 병렬 비교해야 한다.
