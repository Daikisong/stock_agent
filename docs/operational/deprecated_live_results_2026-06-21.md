# Deprecated Live Results - 2026-06-21

아래 결과는 운영 점수로 쓰지 않는다. 이유는 단순히 점수가 낮아서가 아니라, Evidence OS v2가 요구하는 `canonical_archetype_id`, claim-backed component ratio, current/direct/source-backed claim 장부가 없기 때문이다.

쉬운 예: 월덱스 기사 안에 삼성전자가 고객사로 언급됐다고 해서 월덱스의 `감사의견 적정` 문구가 삼성전자의 회계 hard break가 되면 안 된다. 이 결과들은 바로 그 종류의 레거시 오귀속을 막기 위해 폐기됐다.

## 폐기된 Row

- 삼성전자(005930): score=63.2499, stage=4C, red_team=hard_break, reason=missing canonical_archetype_id or claim_backed_component_ratio; legacy 63-point result is not accepted
- SK하이닉스(000660): score=63.8662, stage=3-Red, red_team=moderate, reason=missing canonical_archetype_id or claim_backed_component_ratio; legacy 63-point result is not accepted

## 폐기 사유

- 90점대 잠정 실행과 63점대 레거시 실행은 commit/config/query/corpus/fetch 정책이 달라 `NON_COMPARABLE`이다.
- Green gate 실패는 점수를 90점에서 60점으로 깎는 이유가 아니다. 점수 입력 claim/risk가 바뀐 별도 실행이다.
- `score-gap round_limit_reached` 상태에서 낮은 점수를 최종 운영 점수처럼 확정하면 안 된다.
- 타사 정상 감사의견, 과거 미확인 risk, snippet-only/LLM-only/parser-only field는 운영 점수에 들어가지 않는다.

## 대체 검증 경로

`PYTHONPATH=src python -m e2r.cli.run_agentic_cutover_acceptance` 결과와 `evidence_os_v2_live_smoke_results.json`의 accepted rows를 운영 기준으로 사용한다.
