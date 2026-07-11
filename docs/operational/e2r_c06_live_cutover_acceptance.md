# E2R C06 Canonical Live Cutover Acceptance

- as_of_date: 2026-07-11 KST
- status: C06_CANONICAL_LIVE_CUTOVER_PASS
- Samsung: SAMSUNG_CANONICAL_FULL_THESIS_PASS
- SK Hynix: SK_HYNIX_CANONICAL_FULL_THESIS_PASS
- known-bad: EVIDENCE_TO_SCORE_KNOWN_BAD_PASS (25/25)
- Reviewer A~G: 7/7 PASS
- full unittest: 5,786 PASS, skip/xfail 0
- critical_count_sum: 0
- blockers: []
- investment recommendation emitted: false

## Conversion funnel

| target | fetched docs | raw assertions | organic claims | validated impacts | credited impacts | supported components | evaluated absent | FULL_E2R_100 | Stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 삼성전자 005930 | 5 | 53 | 27 | 32 | 27 | 4 | 3 | 23.639696 | 1 |
| SK하이닉스 000660 | 5 | 53 | 12 | 12 | 7 | 3 | 4 | 7.2 | 1 |

다대다 mapping을 허용하므로 validated impact 수는 organic claim 수보다 클 수 있다. 예를 들어 하나의 실적 claim이 `eps_fcf_explosion`과 `information_confidence`에 서로 다른 bounded impact를 줄 수 있지만, claim credit budget과 중복 경제효과 방지 규칙은 그대로 적용된다.

## Conversion rates

| target | organic accepted claim rate | claim with validated impact rate | impact-to-supported-component coverage | rerouted retained rate | full thesis closure |
|---|---:|---:|---:|---:|---:|
| 삼성전자 | 27/53 = 50.94% | 24/27 = 88.89% | 4/7 = 57.14% | 1/1 = 100% | 7/7 terminal |
| SK하이닉스 | 12/53 = 22.64% | 6/12 = 50.00% | 3/7 = 42.86% | 해당 없음(0건) | 7/7 terminal |

`evaluated absent`는 실패가 아니다. 예를 들어 충분히 조사했지만 현재 FCF 근거를 찾지 못했다면 `UNKNOWN`으로 방치하지 않고 `VERIFIED_ABSENT_AFTER_SEARCH`와 검색 소진 근거를 남기며, 그 component만 0점으로 확정한다.

## Score and Stage integrity

- 두 종목 모두 `profile_id=e2r_2_2_archetype_weight_runtime`을 사용했다.
- 두 종목 모두 `full_score_valid=true`, `score_type=FULL_E2R_100`이다.
- component vector 합계와 total score가 일치한다.
- atomic StageCourt의 claim/impact/component ID와 `stagecourt_trace.json`이 일치한다.
- Stage 결과를 사전에 강제하지 않았으며 실제 deterministic 결과는 두 종목 모두 Stage 1이다.

## Replay and generalization

- C06 historical component replay: PASS, future leakage 0, critical guard accuracy 100%.
- C08 direct order / product-profile guard: PASS.
- C15 issuer pass-through / raw commodity headline guard: PASS.
- wrong-subject와 old-risk-resolved guard: PASS.
- source proxy score count: 0.

## Exact cutover verdict

C06_CANONICAL_LIVE_CUTOVER_PASS
