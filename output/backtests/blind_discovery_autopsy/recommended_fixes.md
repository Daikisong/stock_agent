# Recommended Fixes

## add_search_snapshot

- 일진전기 (103590): no_search_snapshot
- 산일전기 (062040): no_search_snapshot
- 한화에어로스페이스 (012450): no_search_snapshot
- 실리콘투 (257720): no_search_snapshot
- 삼성전자 메모리 리레이팅 (005930): no_search_snapshot
- SK하이닉스 메모리 리레이팅 (000660): no_search_snapshot
- HMM (011200): no_search_snapshot

## manual_review

- HD현대일렉트릭 (267260): stage_not_green_but_detected
- 효성중공업 (298040): stage_not_green_but_detected
- 삼양식품 (003230): detected

## no_action_expected_false_positive

- 씨젠 (096530): outside_expected_window
- 에코프로비엠 (247540): not_in_universe
- 대한전선-like (001440): not_in_universe

## Guardrails

- Stage 3-Green precision remains strict.
- Add source coverage before changing scoring thresholds.
- Fixture proxy is diagnostic only.
