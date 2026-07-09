# E2R Reconstruction Phase 2 — Research Corpus Semantic Compiler

## 판정

`RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS`

이 판정은 과거 연구 문서를 case 단위 구조로 복원하는 Phase 2에만 해당한다. 현재 종목의 점수나 Stage가 준비됐다는 뜻은 아니며, `production_runtime_ready=false`다.

쉬운 예로, 예전 방식은 연구 파일 안에 종목이 다섯 개 있어도 첫 번째 6자리 종목코드만 뽑아 파일 전체를 한 case처럼 취급할 수 있었다. 새 방식은 case·trigger·score simulation 행을 ID로 연결하므로 다섯 종목을 다섯 case로 유지한다.

## canonical 경로

입력은 다음 순서로 읽는다.

1. YAML front matter
2. fenced JSON
3. fenced JSONL
4. fenced CSV
5. Markdown table
6. narrative section
7. handoff prompt는 evidence가 아닌 격리 metadata

핵심 구현은 다음과 같다.

- `research_brain/intelligence_schema.py`: artifact, case, outcome, rule, quarantine schema
- `research_brain/corpus/research_corpus_parser.py`: 전체 파일 parser와 정확한 line span
- `research_brain/corpus/research_case_linker.py`: case/trigger/score/rule/source 실제 ID 연결
- `research_brain/compiler/semantic_case_compiler.py`: canonical case-level compiler
- `cli/compile_e2r_research_intelligence.py`: 공식 bounded compile entrypoint

`text[:24000]`, 파일명 archetype 추정, 첫 symbol 선택, 파일 전체 URL의 case URL 승격은 이 경로에 없다.

## 실제 데이터에서 확인한 동작

V12 registry 2,260개 문서를 공식 CLI로 전부 컴파일했다.

| 항목 | 결과 |
|---|---:|
| artifact | 2,260 |
| structured row | 100,282 |
| structured JSONL row | 38,873 |
| HistoricalResearchCase | 10,920 |
| evaluator-only HistoricalOutcome | 19,031 |
| HistoricalRuleCandidate | 6,255 |
| quarantine | 5,549 |
| explicit linkage error | 1,036 |

quarantine과 linkage error는 숨긴 실패가 아니다. 예를 들어 날짜가 없는 구조화 case는 낮은 신뢰도의 정상 case로 섞지 않고 `MISSING_DATE`로 남긴다. 충돌하는 동일 case ID도 마지막 행으로 몰래 덮어쓰지 않고 두 원천을 추적할 수 있게 남긴다.

실제 C17 loop 15 문서에서는 다음 다섯 case가 별도로 복원됐다.

- 롯데정밀화학 `004000`, 2021-09-01
- 코오롱인더 `120110`, 2021-02-02
- 한화솔루션 `009830`, 2020-08-03
- 애경케미칼 `161000`, 2023-04-11
- 효성화학 `298000`, 2021-05-03

예전처럼 롯데정밀화학 하나만 남지 않는다.

## hard acceptance

| 검사 | 결과 |
|---|---:|
| valid structured JSONL preservation | 100% |
| present company name loss | 0 |
| present trigger date loss | 0 |
| first-symbol collapse | 0 |
| 24k truncation limit | 없음 |
| handoff prompt parsed as case | 0 |
| silent duplicate overwrite | 0 |
| historical case runtime score leak | 0 |
| historical outcome runtime prompt leak | 0 |

골든 코퍼스는 C06/C08/C15 URL-backed 행과 C17/C24/C28 source-proxy 행을 각각 포함한다. 별도 registry 골든 샘플은 canonical archetype 36개를 각 1 case로 포함하며 36/36을 정확히 복원한다.

## narrative fallback 안전성

machine-readable case row가 없는 문서만 narrative provider 대상으로 보낸다. provider 결과는 곧바로 case가 되지 않고 `LLM_DERIVED_UNVERIFIED` quarantine candidate가 된다.

provider가 `score=99`, `stage=3-Green`처럼 점수나 Stage를 출력해도 해당 필드는 제거된다. 쉽게 말해 LLM은 “이 문단이 이런 case일 수 있다”까지만 말할 수 있고, 합격 점수표를 직접 작성할 수 없다.

## 출력

공식 CLI는 다음을 쓴다.

- `corpus/historical_artifacts.jsonl`
- `corpus/structured_rows.jsonl`
- `corpus/historical_cases.jsonl`
- `corpus/historical_outcomes.jsonl`
- `corpus/historical_rules.jsonl`
- `corpus/quarantine.jsonl`
- `corpus/linkage_errors.jsonl`
- `compile_manifest.json`
- `compile_report.md`

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.compile_e2r_research_intelligence \
  --repo-root . \
  --output-root output/research_intelligence/phase2-full \
  --strict true
```

## 아직 통과하지 않은 것

URL 문자열이 있다는 사실만으로 A2나 historical replay ready가 되지 않는다. fetch, content hash, published date, as-of, target directness, exact anchor, case 의미 연결은 Phase 3에서 검증한다.

따라서 이 단계의 source 상태는 `SOURCE_PROXY_ONLY`, `EVIDENCE_URL_PENDING`, `URL_PRESENT_UNVERIFIED`까지다. 과거 outcome은 evaluator-only이며 current planner prompt와 deterministic score에 들어가지 않는다.
