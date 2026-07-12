# C06 semantic cutover v2

## 목적

이번 cutover는 “문서를 많이 모았다”가 아니라 `source → claim → eligibility → impact → fact cluster → subcriterion → component → score → Stage`가 실제 live 삼성전자·SK하이닉스에서도 끊기지 않는지 검증했다.

## 최종 운영 결과

| 항목 | 삼성전자 | SK하이닉스 |
|---|---:|---:|
| question families | 13 | 13 |
| organic accepted claims | 18 | 33 |
| accepted primitive mappings | 22 | 37 |
| proposed / validated impacts | 37 / 37 | 119 / 115 |
| terminal components | 7 / 7 | 7 / 7 |
| gold matched facts | 4 / 4 | 5 / 5 |
| full score | 18.159977 | 19.120509 |
| canonical Stage | 0 | 0 |
| critical | 0 | 0 |

두 종목의 높은 점수나 Green을 목표로 하지 않았다. 점수는 evidence가 충족한 bounded cap만 합산했다.

## live에서 발견해 수리한 핵심 원인

1. DART 검색 결과의 가장 최신 접수번호가 항상 material periodic report는 아니었다. periodic report를 우선하고 원문 전체를 보존했다.
2. 전체 문서가 focus excerpt로 잘리면서 표와 본문 근거가 사라졌다. 저장은 full text, LLM 입력만 bounded context로 분리했다.
3. 한국어 `제한된 공급`, `양산 출하` 같은 표현이 primitive alias를 통과하지 못했다. 종목명이 아니라 일반 의미 alias로 보강했다.
4. adjudication 48건을 한 번에 보내 schema 실패가 났다. 12건씩 chunk하고 모든 batch 결과를 합쳤다.
5. scoring 재시도는 FAIL 상태만 골라 `PASS + invalid proposal`을 놓쳤다. invalid/audit critical도 재시도 대상으로 포함했다.
6. 재시도 LLM이 다른 mapping/primitive를 새로 만들 수 있었다. 허용된 exact pair만 복사하도록 계약을 고정했다.
7. `NEUTRAL + PARTIAL_BRIDGE`가 전역 정책에는 점수가 있는데 component schema에서 누락돼 조용히 0이 됐다. 모든 component direction totality에 NEUTRAL을 포함했다.
8. 현재 shortage support와 향후 capacity expansion counter가 함께 있으면 영원한 `CONTRADICTED_OPEN`이 됐다. C06 공급 대응은 `BOUNDED_NET`으로 같은 component에서 상계한다.
9. scope validator가 명시적으로 거절한 제안을 semantic reconciler가 다시 “미연결 positive proposal”로 세어 전체 질문을 막았다. 명시적 rejection은 점수에서 제외하되, rejection을 absence로 숨기는 guard는 유지했다.
10. material fact ID에 direction과 fact cluster가 빠져 support/counter가 충돌했다. 두 필드를 ID lineage에 포함했다.

쉬운 예: “공급 부족”과 “증설”이 같이 있으면 하나를 삭제하지 않는다. 현재 부족 근거에는 점수를 주고, 증설은 그 점수의 지속 가능성을 낮추는 counter로 같은 장부에 남긴다.

## blind gold와 search adequacy

- production lane은 gold visibility가 `false`이며 gold URL/query/fact 누수는 모두 0이다.
- 독립 gold fact는 9개, qualified match 9개, noncritical recall 1.0, critical miss 0이다.
- 필수 gold route 7개를 모두 기록했다. customer official과 financial revision은 공개 원문 재현 불가 사유를 명시했다.
- live search adequacy는 총 26개 질문, critical 0이다.
- 삼성은 evidence found 5 / adequate absence 8, 하이닉스는 evidence found 7 / adequate absence 6이다.
- `UNKNOWN_UNINVESTIGATED`, `SOURCE_PENDING`, `PROVIDER_PENDING`, `BUDGET_PENDING`, `CONTRADICTED_OPEN`은 최종 component/question에 없다.

## 안전성

- scoring/staging/red-team 코드에 삼성전자·SK하이닉스 종목명 조건을 넣지 않았다.
- LLM은 claim과 impact 후보를 구조화했지만 score와 Stage는 결정론적 엔진이 계산했다.
- Tesla Foundry claim은 C06 allocation을 닫지 않았다.
- substrate profile은 HBM capacity/revenue를 열지 않았다.
- 같은 fact/document의 반복 claim은 cluster와 shared-credit cap으로 중복 점수를 만들지 않는다.
- direct 투자 권고 문구는 생성하지 않는다.

## 재현 위치

- blind gold: `output/evidence_to_score_v2/blind_2026-07-11/gold/`
- blind production: `output/evidence_to_score_v2/blind_2026-07-11/production/`
- 삼성 dossier: `output/evidence_to_score_v2/live_2026-07-11/005930/`
- 하이닉스 dossier: `output/evidence_to_score_v2/live_2026-07-11/000660/`

운영 감사의 직접 leaf는 보고서 counter를 신뢰하지 않아도 각각 다시 읽어 검증할 수 있게 커밋한다.
