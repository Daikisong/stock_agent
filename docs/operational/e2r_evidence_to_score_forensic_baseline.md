# E2R Evidence-to-Score Bridge Forensic Baseline

기준일은 `2026-07-11`이다. 이 문서는 Phase 41 read-only 감사 결과이며 아직 production scoring bridge를 수정하지 않은 상태를 기록한다.

## 1. Production score source of truth

연구 보정 weight의 canonical artifact는 `configs/e2r_archetype_weight_profile_v2_2.json`이다. C06 component weight는 `eps_fcf_explosion=24`, `earnings_visibility=21`, `bottleneck_pricing=19`, `market_mispricing=15`, `valuation_rerating=12`, `capital_allocation=4`, `information_confidence=5`이며 합계는 100이다.

현재 live path는 이 profile을 로드하지 않는다. `CurrentAtomicDecisionBuilder.build()`가 이번 실행의 SourceTask primitive 집합을 score rule 집합으로 만들고 `_balanced_points(len(unique))`를 호출한다.

## 2. Exact root causes

1. `current_atomic_decision.py::CurrentAtomicDecisionBuilder.build`: SourceTask primitive 수로 100점을 균등 분배하고 모든 rule에 material/green-required를 일괄 적용한다.
2. `current_atomic_decision.py::_adapt_direct_current_claims`: `DIRECT_TASK_SATISFIED`와 `original_gap_open=False`만 score claim으로 승격한다.
3. 같은 함수의 `closure_by_claim`: 한 claim이 다른 direct primitive를 닫으면 `current claim closes multiple direct primitives` 오류를 낸다.
4. `current_claim_compiler.py::CurrentClaimCompiler.compile`: `accepted_claims[claim_id]`를 mapping마다 다시 써서 claim row mapping lineage를 단일 mapping으로 축소할 수 있다.
5. `_daily_provenance`: provenance도 mapping 하나만 담은 row를 만들고 후속 code는 claim별 단일 provenance를 기대한다.
6. `atomic_score_stage.py::decide_atomic_score_stage`: material rule의 미충족을 모두 material gap으로 만들며 full score validity를 all-or-nothing으로 판정한다.
7. `live_acceptance.py::run_full_live_acceptance`: controlled Samsung probe를 base Current input에 merge하고 accepted claim 존재를 acceptance hard gate로 사용한다.
8. `live_operational_packager.py::package_live_current_operation`: accepted row와 contribution row가 있으면 score validity와 무관하게 operational envelope를 ready로 만들 수 있다.
9. `final_readiness.py`: 기존 verdict는 mandatory organic `FULL_E2R_100` canary를 요구하지 않는다.

## 3. Mapping and reroute loss

SourceTask satisfaction과 global score semantics가 한 구조로 결합돼 있다. rerouted claim은 원래 질문을 닫지 않는 것은 올바르지만, atomic adapter가 satisfaction status만 읽기 때문에 그 claim이 실제로 지원하는 다른 primitive/component에도 도달하지 못한다. 현재 base run에는 accepted claim 자체가 0건이라 관측된 rerouted score loss는 0건이지만 production-reachable structural loss path는 존재한다.

## 4. Organic and probe separation

- organic base live: accepted claim 0, provenance 0, valid score 0.
- Samsung acceptance probe: accepted claim 1, provenance 1, balanced contribution `16.666667`, `NO_SCORE`, Stage 0.
- canonical Current: probe promotion 후 accepted claim 1이 보이므로 organic과 probe가 결과상 섞여 있다.
- SK Hynix probe: accepted claim 0.

## 5. Current versus calibrated contract

현재 contract는 “질문 6개 = component 6개 = 각 1/6점”이다. calibrated contract는 고정된 7개 경제 component와 연구 기반 weight를 사용해야 한다. SourceTask는 조사 계획일 뿐 score universe가 아니다.

## 6. Phase 41 verdict

`SCORING_BRIDGE_FORENSIC_PASS`다. 이는 결함을 정확히 찾았다는 뜻이며 scoring READY가 아니다. 다음 단계는 legacy path를 production에서 차단하고 canonical scoring contract loader를 연결하는 것이다.
