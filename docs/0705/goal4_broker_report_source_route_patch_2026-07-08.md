# Goal4 Broker Report Source Route Patch - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 Goal4 runtime parity 수리 중 확인한 broker report source route 병목과 이번 패치를 기록한다.

## 결론

이번 패치는 Goal4 완료 패치가 아니다.

수리한 것은 다음 병목이다.

```text
검색/획득 단계:
증권사 리포트 원문 후보를 가져옴

claim extraction 단계:
LLM이 ARR, recurring margin 같은 직접 claim을 뽑음

score eligibility 단계:
그 문서가 verified report original로 전달되지 않아
general web search source로 오해되고 claim이 버려짐
```

쉬운 예:

```text
증권사 리포트 PDF에서 "ARR 성장" 문장을 찾았다.
그런데 채점창구가 "이건 그냥 검색 결과니까 점수 근거로 못 씀"이라고 반려했다.
```

이번 패치는 이 중 "검증된 리포트 원문 경로인데 일반 검색 출처로 반려되는 문제"를 줄인다.

## 확인한 runtime 증거

최신 기준 output root:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z
```

C28 더존비즈온 사례에서 이미 다음 claim 후보가 있었다.

```text
symbol = 012510
archetype = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
source_url = https://bbn.kiwoom.com/rfCR10848
mapped_primitive_id = arr_growth_visible
mapping_status = ACCEPTED
semantic_status = PASS
target_scope_status = DIRECT
temporal_status = CURRENT
```

하지만 기존에는 아래 이유로 score eligible이 아니었다.

```text
source_task_provider_error_score_block:general_search_not_score_source
source_provider_document_type_mismatch:BrokerReportPublicPDF:general_web_search_provider
source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider
```

즉 문장 자체는 맞게 뽑혔지만, source lineage가 "verified broker report original"로 닫히지 않아 버려졌다.

## 코드 패치

수정 파일:

```text
src/e2r/sources/report_search.py
tests/test_sources.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

새로 verified report original로 인정한 무료 접근 경로:

```text
1. eugenefn.com/common/files/amail/*.pdf
2. bbn.kiwoom.com/rfCR...
3. securities.miraeasset.com/bbs/board/message/view.do?categoryId=1521&messageId=...
```

중요한 점:

```text
도메인 전체를 연 것이 아니다.
리서치 원문으로 쓰이는 좁은 route만 열었다.
```

예:

```text
허용:
https://bbn.kiwoom.com/rfCR10848

불허:
일반 블로그, 종목 게시판, 고객센터 약관 PDF, 이벤트 PDF
```

## 왜 Goal4에 중요하나

C28은 ARR, RPO, renewal, retention 같은 claim이 리포트에 자주 나온다.

그런데 운영 경로가 다음처럼 막히면 C28은 계속 0 accepted claim으로 남는다.

```text
리포트 발견
→ 원문 fetch
→ ARR claim 추출
→ source lineage 미검증으로 폐기
→ C28 accepted claim 0
```

이번 패치 후에는 다음 경로가 가능하다.

```text
리포트 발견
→ verified broker report original lineage 부여
→ ARR claim 추출
→ source eligibility 통과
→ accepted claim 생성 가능
```

테스트에서 `bbn.kiwoom.com/rfCR...` 경로는 C28 `arr_growth_visible` claim을 accepted claim으로 만들 수 있음을 확인했다.

## 이 패치가 해결하지 않는 것

여전히 남은 문제:

```text
C08 리노공업: 리포트 원문을 일부 가져왔지만 고객 품질/qualification/repeat order claim이 아직 직접 accepted 되지 않음
C15 KG케미칼: accepted claim은 있으나 spread -> realized margin -> cash/revision 사슬이 아직 material gap
C06/C17: production score path는 있으나 required-positive/Green gap 남음
전체 C01~C32/C36 meaningful runtime parity는 아직 미완료
```

쉬운 예:

```text
이번 패치는 "유효한 리포트 서류를 접수창구가 제대로 받아주게 한 것"이다.
서류 안에 필요한 문장이 없거나, LLM이 직접 claim을 못 뽑으면 여전히 점수는 0이어야 한다.
```

## 검증

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests/test_sources.py \
  tests/test_research_brain_v4_real_source_acquisition.py \
  tests/test_research_brain_v4_evidence_extraction_from_real_document.py \
  -v

PYTHONPATH=src python -m unittest \
  tests/test_research_to_runtime_parity_goal4.py \
  tests/test_all_archetype_runtime_status_matrix.py \
  tests/test_all_archetype_next_attempt_plan.py \
  tests/test_research_to_runtime_replay_mandatory_archetypes.py \
  -v
```

결과:

```text
source/acquisition/extraction tests: 96 passed
Goal4 linked tests: 34 passed
```

## 다음 작업

다음 runtime attempt 전에 우선순위는 다음이다.

```text
1. C28 next attempt를 돌려 broker report ARR claim이 실제 production accepted claim으로 승격되는지 확인
2. C08은 source route 문제가 아니라 claim 내용/target primitive 문제인지 계속 분해
3. C15는 accepted claim이 어느 primitive에서 멈췄는지 score contribution ledger까지 추적
4. C01~C32 전체에서 source_lineage_unverified_original 때문에 버려진 accepted mapping 후보를 전수 집계
```

현재 Goal4 상태는 계속 다음이다.

```text
MEANINGFUL_RUNTIME_PARITY_NOT_READY
```
