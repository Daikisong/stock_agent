# E2R Evidence-to-Score 현재 상태 재분류

- 기준일: `2026-07-11`
- 기존 live materialization: `LIVE_MATERIALIZATION_AND_FAIL_CLOSED_PIPELINE_PASS`
- organic evidence-to-score bridge: `ORGANIC_EVIDENCE_TO_SCORE_BRIDGE_NOT_READY`
- meaningful scoring: `MEANINGFUL_E2R_SCORING_NOT_READY`

canonical KRX universe, bounded source acquisition, document/anchor/hash/quote 검증은 실제로 동작한다. 그러나 base live run의 organic accepted claim은 0건이고 `score_valid=true` 결정도 0건이다. 현재 canonical Current의 accepted claim 1건은 `claim_probe_samsung_q1`에서 promotion된 controlled acceptance probe다.

## 확인된 단절

- `CurrentAtomicDecisionBuilder`는 canonical C06 weight profile 대신 `_balanced_points()`로 SourceTask primitive 6개에 `16.666667`점씩 나눈다.
- 생성된 모든 primitive rule은 `material=True`, `green_required=True`다.
- atomic claim adapter는 `DIRECT_TASK_SATISFIED`만 읽고 rerouted mapping의 전역 점수 효용을 버린다.
- accepted claim dictionary는 동일 claim의 mapping을 순회하며 `mapping_ids=[현재 mapping 하나]`로 덮어쓸 수 있다.
- 모든 material primitive가 SATISFIED가 아니면 확인된 contribution이 있어도 `NO_SCORE / Stage 0`이 된다.
- 기존 final readiness는 organic full score 없이 acceptance probe claim/provenance/contribution만으로 통과할 수 있다.

## 현재 관측치

| 경로 | accepted claim | score contribution | `score_valid=true` | `FULL_E2R_100` |
|---|---:|---:|---:|---:|
| base live materialization | 0 | 0 | 0 | 0 |
| Samsung controlled probe | 1 | 1 | 0 | 0 |
| canonical Current after probe promotion | 1 | 1 | 0 | 0 |
| SK Hynix controlled probe | 0 | 0 | 0 | 0 |

삼성전자 probe claim은 실제 공식 2026년 1분기 실적 문서의 ASP·사상 최대 매출/영업이익 문장을 사용하지만, organic base run에서 생성된 claim이 아니며 현재 점수는 `NO_SCORE`다. 따라서 새 scoring READY의 근거로 계산하지 않는다.
