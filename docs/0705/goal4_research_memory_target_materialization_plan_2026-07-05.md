# Goal4 Research Memory Target Materialization Plan - 2026-07-05

이 문서는 Goal4의 다음 병목을 고정한다.

## 결론

이번 패치는 Goal4 완료가 아니다. 대신 이전 상태에서 가장 큰 구멍이던 `targetless archetype shell`을 연구자료 기반의 실제 심볼 후보로 바꿨다.

쉬운 예:

```text
이전:
  C08이라는 진료과만 있음
  실제 환자 이름/주민번호가 없음
  그래서 검사를 했다고 말하면 안 됨

이번:
  C08 진료과에 058470이라는 환자 후보를 붙임
  단, 과거 연구자료는 진단서가 아니라 예약 메모임
  현재 공시/IR/뉴스에서 다시 검사해야 점수에 들어감
```

핵심 안전장치:

```text
research_memory_target_candidate != score evidence
```

즉 연구자료가 심볼 후보를 만들 수는 있지만, 점수와 Stage는 current source-backed Evidence OS claim이 생기기 전까지 막힌다.

## 이번에 고친 문제

직전 0705/0706 문서 기준 next attempt plan은 다음 상태였다.

```text
target_symbol_mode_counts:
  ARCHETYPE_LEVEL_DISCOVERY = 32
  SYMBOL_SPECIFIC = 4

target_materialization_required_task_count = 96
```

문제는 C08/C15/C17/C24/C28 같은 아키타입에 연구자료와 replay case가 있는데도 다음 실행 plan에서는 실제 심볼 없이 아키타입 단위 discovery로만 남았다는 점이다.

그 결과 다음 실행이 이렇게 될 수 있었다.

```text
C08 source task 실행
-> symbol 없음
-> 원문 claim을 어느 회사에 붙일지 모름
-> accepted claim/full thesis로 닫을 수 없음
```

이번 패치는 `docs/operational/research_reverse_case_inventory.json`를 읽어, 각 아키타입의 과거 연구자료에서 실제 심볼 후보를 뽑는다.

단, 이 후보는 다음 실행 입력일 뿐이다.

```text
허용:
  C08 다음 조사 대상 = 058470

금지:
  C08 연구자료에 058470이 있었으니 현재 점수 부여
```

## 새 산출물 수치

재생성된 파일:

```text
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/all_archetype_next_runtime_attempt_plan.json
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
```

새 summary:

```text
plan_row_count = 36
source_task_count = 111
seed_event_count = 111

target_symbol_mode_counts:
  ARCHETYPE_LEVEL_DISCOVERY = 3
  RESEARCH_MEMORY_TARGET_CANDIDATE = 29
  SYMBOL_SPECIFIC = 4

research_memory_target_materialized_archetype_count = 29
research_memory_target_materialized_task_count = 87
target_materialization_unresolved_archetype_count = 3
target_materialization_required_task_count = 9
```

해석:

```text
이전에는 32개가 "실제 종목 없음" 상태였다.
이번에는 29개가 연구자료 기반 실제 후보 심볼을 얻었다.
아직 targetless로 남은 것은 R13 공통 guardrail 3개다.
```

## 아키타입별 다음 target 상태

| archetype | target mode | symbols | research source quality | score evidence allowed |
|---|---|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | SYMBOL_SPECIFIC | 052400 | - | false |
| C02_POWER_GRID_DATACENTER_CAPEX | RESEARCH_MEMORY_TARGET_CANDIDATE | 033100 | A2_URL_BACKED | false |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | RESEARCH_MEMORY_TARGET_CANDIDATE | 047810 | A2_URL_BACKED | false |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | RESEARCH_MEMORY_TARGET_CANDIDATE | 011700 | A2_URL_BACKED | false |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | SYMBOL_SPECIFIC | 003380 | - | false |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | SYMBOL_SPECIFIC | 005930 | - | false |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | RESEARCH_MEMORY_TARGET_CANDIDATE | 031980 | A2_URL_BACKED | false |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | RESEARCH_MEMORY_TARGET_CANDIDATE | 058470 | A2_URL_BACKED | false |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | RESEARCH_MEMORY_TARGET_CANDIDATE | 039030 | A2_URL_BACKED | false |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | RESEARCH_MEMORY_TARGET_CANDIDATE | 064760 | A2_URL_BACKED | false |
| C11_BATTERY_ORDERBOOK_RERATING | RESEARCH_MEMORY_TARGET_CANDIDATE | 003670 | A2_URL_BACKED | false |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | RESEARCH_MEMORY_TARGET_CANDIDATE | 051365 | A2_URL_BACKED | false |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | RESEARCH_MEMORY_TARGET_CANDIDATE | 020150 | A2_URL_BACKED | false |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | RESEARCH_MEMORY_TARGET_CANDIDATE | 002710 | A2_URL_BACKED | false |
| C15_MATERIAL_SPREAD_SUPERCYCLE | RESEARCH_MEMORY_TARGET_CANDIDATE | 001390 | A2_URL_BACKED | false |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RESEARCH_MEMORY_TARGET_CANDIDATE | 005290 | A2_URL_BACKED | false |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | RESEARCH_MEMORY_TARGET_CANDIDATE | 011170 | A2_URL_BACKED | false |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | RESEARCH_MEMORY_TARGET_CANDIDATE | 278470 | A2_URL_BACKED | false |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | RESEARCH_MEMORY_TARGET_CANDIDATE | 383220 | EVIDENCE_URL_PENDING | false |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | RESEARCH_MEMORY_TARGET_CANDIDATE | 257720 | EVIDENCE_URL_PENDING | false |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | RESEARCH_MEMORY_TARGET_CANDIDATE | 055550 | A2_URL_BACKED | false |
| C22_INSURANCE_RATE_CYCLE_RESERVE | RESEARCH_MEMORY_TARGET_CANDIDATE | 000810 | A2_URL_BACKED | false |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | RESEARCH_MEMORY_TARGET_CANDIDATE | 000100 | A2_URL_BACKED | false |
| C24_BIO_TRIAL_DATA_EVENT_RISK | RESEARCH_MEMORY_TARGET_CANDIDATE | 000100 | SOURCE_PROXY_ONLY | false |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | RESEARCH_MEMORY_TARGET_CANDIDATE | 043150 | A2_URL_BACKED | false |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | RESEARCH_MEMORY_TARGET_CANDIDATE | 035420 | A2_URL_BACKED | false |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | RESEARCH_MEMORY_TARGET_CANDIDATE | 035760 | A2_URL_BACKED | false |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | RESEARCH_MEMORY_TARGET_CANDIDATE | 012510 | A2_URL_BACKED | false |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | SYMBOL_SPECIFIC | 017670, 024110 | - | false |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | RESEARCH_MEMORY_TARGET_CANDIDATE | 006360 | A2_URL_BACKED | false |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | RESEARCH_MEMORY_TARGET_CANDIDATE | 051910 | A2_URL_BACKED | false |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | RESEARCH_MEMORY_TARGET_CANDIDATE | 000670 | A2_URL_BACKED | false |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | ARCHETYPE_LEVEL_DISCOVERY | - | - | false |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | ARCHETYPE_LEVEL_DISCOVERY | - | - | false |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | RESEARCH_MEMORY_TARGET_CANDIDATE | 010130 | PRICE_PATH_ONLY | false |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | ARCHETYPE_LEVEL_DISCOVERY | - | - | false |

중요한 해석:

```text
C01~C32는 이제 모두 다음 실행에서 실제 symbol이 있다.
하지만 C19/C20/C24/R13_HIGH_MAE처럼 source quality가 약한 후보도 있다.
그래서 모든 row는 score evidence allowed = false다.
```

## C24 같은 source proxy 후보를 왜 허용했나

C24는 현재 가장 조심해야 하는 사례다.

```text
C24 target candidate = 000100
support source quality = SOURCE_PROXY_ONLY
score_evidence_allowed_from_research = false
```

이건 "000100을 C24로 점수화해도 된다"가 아니다.

정확한 의미:

```text
과거 C24 연구자료에서 000100이 자주 등장했다.
그러니 다음 C24 live/source task는 000100을 한 번 공식-first로 확인해라.
다만 그 연구자료 자체는 운영 점수에 넣지 마라.
```

쉬운 예:

```text
누가 "이 환자는 임상 리스크로 봐야 할 수 있다"고 메모해 둠
-> 병원 접수에는 올릴 수 있음
-> 하지만 그 메모만으로 진단명 확정은 불가
-> 현재 검사 결과가 필요함
```

## 코드 안전장치

변경 파일:

```text
src/e2r/census/all_archetype_next_attempt_planner.py
src/e2r/census/placeholder_symbols.py
tests/test_all_archetype_next_attempt_plan.py
```

추가된 안전장치:

```text
1. research_reverse_case_inventory.json을 optional input으로 로드
2. canonical_archetype_id가 같은 연구 case만 후보로 사용
3. docs/round 직접 아키타입 파일과 A2_URL_BACKED case를 우선
4. 000000, 111111 같은 반복 숫자 placeholder symbol 제외
5. 후보 row에 score_evidence_allowed_from_research = false 강제
6. source task query intent에 "Treat this only as a target candidate" 명시
7. 모든 materialized task는 current source confirmation required
8. 점수/stage promotion은 source-backed claim 전까지 false
```

## 테스트로 고정한 것

추가/수정된 테스트는 다음을 확인한다.

```text
1. C08/C15/C17/C24/C28이 실제 후보 symbol을 갖는다.
2. 그 후보는 score evidence로 허용되지 않는다.
3. C01~C32 전체가 더 이상 target materialization unresolved가 아니다.
4. materialized source task 87개가 모두 planner input only다.
5. hardcoded query는 0개다.
6. 모든 task는 finite budget을 가진다.
```

실행 결과:

```bash
PYTHONPATH=src python -m unittest tests.test_all_archetype_next_attempt_plan -v
```

```text
Ran 7 tests in 0.293s
OK
```

전체 회귀 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

```text
Ran 5254 tests in 424.029s
OK
```

재생성 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass --as-of-date 2026-07-05 --fail-on-c05-monoculture true --fail-on-unknown-target-promoted true --fail-on-required-positive-missing-over-threshold true --fail-on-research-proxy-score true
```

결과:

```text
exit code = 2
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
failed_on = C05_FULL_THESIS_MONOCULTURE, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

이 실패는 정상이다. 이번 패치는 Goal4 합격 선언이 아니라 다음 실행 입력을 더 정확하게 만든 것이다.

## 아직 Goal4 완료가 아닌 이유

남은 blocker:

```text
1. production full thesis row는 C05/C06 score path 중심이다.
2. promoted row는 required positive primitive가 비어 있다.
3. C08/C15/C17/C24/C28은 이제 target 후보가 생겼지만 아직 current accepted claim/full thesis가 아니다.
4. R13 공통 guardrail 3개는 여전히 archetype-level discovery다.
5. source proxy / evidence pending 연구자료는 운영 점수 정답으로 쓸 수 없다.
```

쉬운 예:

```text
이번 작업:
  환자 후보 명단을 만들었다.

아직 필요한 작업:
  각 환자에게 실제 검사를 하고
  검사 결과지를 claim ledger에 붙이고
  그 claim으로 StageCourt를 통과시키는 것
```

## 다음 에이전트가 검증해야 할 것

다음 작업은 이 plan을 실제 runtime 실행에 넣어 확인해야 한다.

필수 확인:

```text
1. RESEARCH_MEMORY_TARGET_CANDIDATE seed가 CensusV4에서 실제 symbol-specific source task로 실행되는가
2. source_proxy_only 후보가 점수에 들어가지 않고 current source recheck로만 쓰이는가
3. C08/C15/C17/C24/C28에서 accepted claim이 생기면 full thesis 재시도가 되는가
4. accepted claim이 없으면 낮은 점수 확정이 아니라 Source/Provider Pending으로 남는가
5. R13 targetless guardrail 3개는 별도 target materialization 전략이 필요한가
```

최종 목표는 변하지 않았다.

```text
모든 아키타입:
research memory -> current source route -> Evidence OS accepted claim -> score contribution -> StageCourt
```

이번 패치는 그중 첫 번째 막힌 지점인 `target company/ticker materialization`을 C01~C32에 대해 연 것이다.
