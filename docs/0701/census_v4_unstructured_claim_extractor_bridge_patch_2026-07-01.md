# Census v4 Unstructured Claim Extractor Bridge Patch - 2026-07-01

이 문서는 `web/news/IR/report` full-source 원문이 `EvidenceDocument`로 fetch되어도
accepted claim까지 이어지지 않던 병목에 대한 2차 패치 기록이다.

## 결론

이번 패치로 새로 닫은 다리:

```text
TEXT_SPAN EvidenceDocument
-> contract-blind extractor run
-> RawAssertion
-> target/temporal adjudication
-> PrimitiveMapping
-> derive_score_eligibility
-> accepted/rejected claim
-> claim_extractor_runs.jsonl export
```

아직 닫지 않은 것:

```text
실제 Codex/LLM provider를 canonical run에서 성공시키기
Brain/Web strict promotion
Samsung/Hynix C06 full thesis 실행
전 아키타입 source-backed replay parity
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

쉬운 예:

```text
이전:
  웹 기사 원문 상자는 도착했지만 상자를 열어 claim 장부에 쓰는 사람이 없었다.

이번:
  TEXT_SPAN 원문이면 contract-blind extractor가 상자를 열고 raw assertion을 만든다.
  다만 테스트용 rule fallback은 운영 LLM pass로 인정하지 않는다.
```

## 구현 파일

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/census/census_runner_v4.py
src/e2r/production/claim_extraction/contract_blind_extractor.py
src/e2r/production/claim_extraction/primitive_mapper.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_brain_web_readiness_gate.py
tests/test_cutover_contract_blind_extraction.py
```

## Bridge 변경

기존 `v4_evidence_extraction_bridge`의 병목:

```python
row = normalized.get("row") if isinstance(normalized.get("row"), Mapping) else {}
if not row:
    return ()
```

즉 structured API row가 없는 web/news 원문은 `mention_only`로 끝났다.

패치 후:

```text
structured row 있음
  -> 기존 structured extraction 유지

structured row 없음 + anchor_type=TEXT_SPAN + document_text 있음
  -> LLMContractBlindRawAssertionExtractor.extract_with_metadata()
  -> RawAssertionRecord
  -> exact quote/span validation
  -> AdjudicatedClaim
  -> map_claim_to_primitive()
  -> derive_score_eligibility()
```

중요 원칙:

```text
extractor는 primitive_gap, score, stage, green gate를 보지 않는다.
extractor run row에는 input_context_keys와 forbidden_context_seen을 남긴다.
score eligibility는 LLM 출력이 아니라 deterministic guard가 파생한다.
```

## claim_extractor_runs leaf

`EvidenceOSExecutionBundleV4`에 아래 leaf가 추가됐다.

```text
claim_extractor_runs
```

`_export_brain_web_bundle_leafs()`가 이를 export한다.

```text
output/census_v4/YYYY-MM-DD/claim_extractor_runs.jsonl
```

row 주요 필드:

```text
claim_extractor_run_id
candidate_event_id
symbol
document_id
anchor_id
provider_name
provider_mode
model
prompt_hash
response_hash
status
provider_error
input_context_keys
forbidden_context_seen
raw_assertion_ids
raw_assertion_count
source_origin=research_brain_v4_attempt
```

## Provider failure 분리

extractor provider가 실패하면 이제 `NO_EVIDENCE_FOUND`가 아니다.

```text
provider_error 있음
-> SourceTaskExecution.status = PROVIDER_FAILED
-> provider_errors에 claim_extractor_provider_error 기록
-> accepted_claim_ids 없음
```

쉬운 예:

```text
기사를 못 찾은 것과, 기사를 가져왔지만 독해 LLM이 죽은 것은 다르다.
전자는 no evidence일 수 있지만 후자는 ProviderFailed/Pending이다.
```

## Rule fallback은 운영 pass 근거가 아님

현재 default `LLMContractBlindRawAssertionExtractor`는 테스트 가능성을 위해
`RuleFallbackExtractorProvider`를 쓸 수 있다.

이 fallback은:

```text
unit test / diagnostic용
```

이지,

```text
BRAIN_WEB_EVIDENCE_PASS 근거
```

가 아니다.

그래서 readiness gate를 강화했다.

```text
accepted Brain/Web claim이 있고
claim_extractor_runs가 있지만
provider_mode=llm run이 0개이면
-> BLOCKED
```

새 blocker:

```text
LLM claim extractor has no real LLM provider runs
```

새 audit fields:

```text
llm_claim_extractor_real_provider_count
claim_extractor_non_llm_provider_count
claim_extractor_forbidden_context_count
```

쉬운 예:

```text
연습용 자동 밑줄 긋기로 claim 후보를 만들 수는 있다.
하지만 실제 운영 통과는 LLM 독해 기록이 있어야 한다.
```

## Fallback predicate 보강 범위

테스트용 fallback extractor는 아래 정도의 HBM 원문을 raw assertion으로 만들 수 있게 했다.

```text
삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다.
```

이는 운영 점수 하드코딩이 아니다.

이유:

```text
1. extractor는 score/stage/primitive_gap을 보지 않는다.
2. mapper/eligibility를 통과해야 한다.
3. provider_mode=rule_fallback이면 Brain/Web readiness pass를 막는다.
```

운영에서는 실제 provider_mode=llm extractor run이 필요하다.

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_cutover_contract_blind_extraction -v
```

결과:

```text
Ran 28 tests in 7.272s
OK
```

검증된 것:

```text
1. structured API row 기존 경로 유지
2. TEXT_SPAN mention-only는 점수/claim으로 안 들어감
3. TEXT_SPAN HBM customer allocation 문장은 RawAssertion -> accepted claim으로 이어짐
4. extractor provider error는 PROVIDER_FAILED로 남음
5. web fetched document bundle export가 claim_extractor_runs.jsonl도 export
6. rule_fallback extractor claim만으로는 Brain/Web evidence pass 불가
7. extractor forbidden context guard 기존 테스트 유지
```

## 남은 병목

이번 패치는 pipeline bridge다.

아직 운영 완료가 아닌 이유:

```text
canonical output/census_v4/2026-07-01은 여전히 Brain/Web disabled run이다.
planner_runs/web_search/claim_extractor canonical row는 아직 0개다.
실제 LLM provider success와 strict promotion은 아직 검증되지 않았다.
Samsung/Hynix full thesis task는 아직 executed trace가 아니다.
```

다음 패치 순서:

```text
1. Brain/Web enabled smoke에서 real LLM extractor provider를 연결한다.
2. prompt/response leaf를 claim_extractor_runs와 연결한다.
3. accepted claim -> score contribution -> StageCourt -> brain_to_claim_trace를 strict promotion 전까지 닫는다.
4. Samsung/Hynix full thesis source task를 planning-only에서 executed/pending truth state로 이동한다.
5. canonical output을 재생성하고 Brain/Web readiness gate를 다시 평가한다.
```

## 금지 문장

이번 패치 후에도 아래 문장은 틀리다.

```text
Brain/Web evidence pass가 끝났다.
LLM extractor가 운영에서 성공했다.
Samsung/Hynix full thesis Stage가 나왔다.
canonical run에 web/news accepted claim이 반영됐다.
```

허용 문장:

```text
unstructured TEXT_SPAN 원문을 contract-blind extraction path로 claim ledger에 연결하는 코드 경로와 테스트가 추가됐다.
rule fallback은 운영 pass 근거가 아니며 readiness gate에서 차단된다.
```

