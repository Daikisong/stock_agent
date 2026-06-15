# Score Validity Route Block Audit - 2026-06-12

## 문제

삼성전자, SK하이닉스 운영형 테스트에서 점수가 80점대와 60점대로 급변해 보였다.

원인은 실제 점수 모델이 같은 조건에서 바뀐 것이 아니라, 서로 다른 상태가 같은 `score_total` 숫자로 표시된 것이다.

- 정상 케이스: LLM theme route가 source-backed 아키타입을 확정한 뒤 점수 산출
- 문제 케이스: LLM route가 `provider_error` 또는 `needs_more_evidence`인데도 raw fallback 성격 점수가 정상 점수처럼 노출

예:

- 정상: `C06_HBM_MEMORY_CUSTOMER_CAPACITY` 확정 후 80점대
- 비정상 표시: provider_error 상태인데 60점대 score_total처럼 표시

## 적용한 불변식

운영형 theme rebalance가 켜져 있고 theme route provider가 있으면, 아래 조건 없이는 최종 점수를 유효로 보지 않는다.

- route status가 `transition_detected` 또는 `mixed_route`
- route confidence가 0.55 이상
- `canonical_archetype_id`가 존재
- source-backed evidence slot이 존재
- route ID가 실제 scoring payload에 적용됨

위 조건을 못 맞추면 다음처럼 처리한다.

- `score_valid=false`
- `score_total=null`로 출력
- raw 참고값은 `raw_score_total_before_theme_route_block`에만 보관
- canonical stage는 `0`
- `stage_reason`은 route unresolved 차단 사유를 표시
- unconfirmed `scoring_large_sector_id`, `scoring_canonical_archetype_id`는 `null`

## 전역 차단 위치

1. FreeWebResearchRunner
   - route 실패, low confidence, source-backed evidence 없음, provider_error를 final score/stage 직전에 차단한다.

2. StageClassifier
   - 어떤 호출자가 무효 score를 다시 classify해도 `score_valid=0`이면 Stage 0으로 고정한다.
   - 회사 이벤트 점수가 높아도 Stage 1/2/3으로 부활하지 않는다.

3. CompanyResearchPipeline
   - FreeWeb 확장 결과가 route block이면 StageUpdateEngine으로 다시 분류하지 않고 blocked stage를 유지한다.

4. 출력/요약
   - Korea live targeted smoke row: `score_total=null`, `score_valid=false`
   - Morning brief: `총점 0.0` 대신 `점수 산출 보류`
   - Daily scan JSON: `score=null`, `score_valid=false`
   - As-of replay web-only score: invalid score는 `null`
   - As-of replay merged score: web score가 invalid면 merged score도 `null`
   - E2R standard replay score: invalid score는 `null`
   - Blind discovery CSV: invalid score는 빈 칸, JSON은 `null`

## 운영형 확인

### 삼성전자

2026-06-12 route-block 패치 직후 운영형 target smoke 재실행 결과:

- route: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- route evidence gate: `source_backed`
- `score_valid=true`
- `score_total=68.9388`
- stage: `2`

이 결과는 route failure 둔갑 문제가 아니었다. 다만 80점대가 아닌 이유는 별도 점수 항목 문제였다.

확인된 약점:

- selected FCF source 없음
- selected revision source 없음
- earnings visibility, bottleneck/pricing, valuation 일부 감점

이후 score-gap block 패치를 추가했다. 따라서 같은 상태에서 LLM score-gap 확장이 새 검색을 만들지 못하거나 provider_error로 끝나면 더 이상 `68점 Stage2` 같은 최종 결과로 내보내지 않는다.

새 기준:

- `score_valid=false`
- `score_total=null`
- raw 참고값은 `raw_score_total_before_score_gap_block`에 보관
- canonical stage는 `0`
- `score_blocked_reason=score_gap_*`

### SK하이닉스

2026-06-12 provider timeout 검증 결과:

- `theme_rebalance_status=provider_error`
- `score_total=null`
- `score_valid=false`
- `score_blocked_reason=theme_route_provider_error`
- `raw_score_total_before_theme_route_block=41.9318`
- `scoring_canonical_archetype_id=null`
- status: `score_blocked_theme_route`

따라서 이제 provider_error 상태가 40점대, 60점대, 80점대 같은 정상 점수로 보이지 않는다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_staging tests.test_company_research_expansion tests.test_free_web_research_runner tests.test_korea_live_lite tests.test_briefing -v`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- `PYTHONPATH=src python -m compileall -q src tests`
- route 상태 조합 30개 정적 검증
- score-gap block 상태 조합 41개 정적 검증
- as-of merged score block 상태 조합 4개 정적 검증
- SK하이닉스 provider-timeout 운영형 검증

전체 테스트 결과:

- 3,765 tests passed

## 남은 별도 리스크

이번 패치는 두 가지 둔갑 문제를 막는다.

- 실패한 route가 정상 점수처럼 보이는 문제
- 유효 route 이후 핵심 score source가 비었는데 낮은 정상 점수처럼 보이는 문제

아직 별도 개선이 필요한 부분:

- valid route 이후 LLM이 더 좋은 검색어를 만들어 실제 EPS/OP/FCF/revision/valuation source를 채우는 품질
- 검색 provider가 실제 증권사 리포트/컨센서스 페이지를 얼마나 잘 회수하는지

즉 앞으로 봐야 할 문제는 "점수 둔갑"이 아니라 "보류된 score-gap을 실제 evidence로 얼마나 잘 해소하는가"다.

## 2026-06-12 추가 보강: 유효 route 이후 핵심 source 누락

삼성전자처럼 route는 유효한데 selected FCF source, selected revision source가 비어 있으면 점수가 낮게 나올 수 있다.

이 문제는 route 실패와 다르다. route는 맞지만 점수 입력 축이 덜 채워진 상태다.

추가 적용한 불변식:

- selected revision source가 없으면 `estimate_missing_revision_source=100`
- selected FCF source가 없으면 `estimate_missing_fcf_source=100`
- selected OP source가 없으면 `estimate_missing_op_source=100`
- 위 진단은 post-score gap context에 직접 들어간다.

예:

- route: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- selected_revision_source: 없음
- selected_fcf_source: 없음

이제 이 상태는 그냥 낮은 점수로 끝나지 않고 LLM에게 다음 축을 다시 찾게 한다.

- analyst consensus revision
- EPS, OP, FCF estimate change
- target price change
- free cash flow estimate
- operating cash flow conversion
- guidance/report/consensus source

운영 로그 보강:

- `post_score_gap_expansion_count`
- `post_score_gap_expansion_queries`

따라서 `post_parse_gap_expansion_count=0`이어도 post-score 단계에서 무엇을 다시 검색했는지 볼 수 있다.

## 2026-06-12 추가 보강: score-gap 실패 차단

score-gap 확장이 켜져 있는데 핵심 source가 비어 있으면, final score/stage 직전에 한 번 더 확인한다.

보류 대상 material gap:

- `selected_eps_source_missing`
- `selected_revision_source_missing`
- `selected_fcf_source_missing`
- `selected_operating_profit_source_missing`
- date-unverified/snippet-only/emerging-theme deep research 미완료처럼 source 품질 문제인 gap

LLM이 이 gap을 보고도 아래 상태로 끝나면 정상 점수로 인정하지 않는다.

- `provider_error`
- `invalid_provider_output`
- `disabled_no_provider`
- `llm_no_suggested_queries`
- `no_executable_searches`
- `budget_blocked`
- search provider block/timeout 계열

처리 방식:

- `score_valid=false`
- `score_blocked_by_score_gap=100`
- `score_blocked_reason=score_gap_*`
- `score_total=null`로 출력
- raw 참고값은 `raw_score_total_before_score_gap_block`
- StageClassifier는 `score_valid=0`을 보고 Stage 0으로 고정
- CompanyResearchPipeline은 blocked stage를 StageUpdateEngine으로 재분류하지 않음

쉬운 예:

- 예전: "FCF/revision 소스를 못 찾음 -> 68점 Stage2"
- 지금: "FCF/revision 소스를 못 찾았고 LLM 확장도 새 검색을 못 만듦 -> score pending, raw 68점 참고"

반대로 실제 검색을 통해 EPS/OP/FCF/revision source가 채워지면 정상 score/stage 분류로 넘어간다.

## 2026-06-12 추가 보강: Codex provider timeout 정리

Codex route provider는 `subprocess.run` 대신 별도 process group 실행으로 변경했다.

이유:

- Codex CLI가 내부 하위 프로세스를 만들 수 있다.
- timeout 때 직접 프로세스만 죽으면 하위 프로세스가 남아 다음 운영 실행에 영향을 줄 수 있다.

새 처리:

- timeout 발생 시 process group 전체에 `SIGTERM`
- 5초 내 종료되지 않으면 `SIGKILL`
- pipeline에는 `provider_error / codex_cli_timeout`으로 반환
- 이 상태는 theme-route 또는 score-gap block으로 이어져 정상 점수처럼 노출되지 않는다.

## 2026-06-12 추가 보강: as-of merged replay 재승격 차단

as-of replay는 원래 두 점수를 볼 수 있다.

- `web_only_score`: FreeWebResearchRunner가 만든 web research 점수
- `merged_score`: official price/disclosure/financial + web evidence를 다시 합친 점수

문제 가능성:

- web research는 LLM route/provider/score-gap 문제로 `score_valid=false`
- 그런데 merged scoring이 official evidence만 보고 새 점수를 만들면 `Stage2` 같은 정상 후보로 다시 살아날 수 있음

새 불변식:

- `web_result.pipeline_result.score`가 invalid면 merged score도 invalid로 처리
- raw merged 점수는 `raw_score_total_before_asof_web_block`에만 보관
- `score_blocked_by_asof_web=100`
- canonical stage는 `0`
- as-of replay CSV/JSON의 `score`, `merged_score`는 `null` 또는 빈 칸
- autopsy markdown/CSV의 `current_score`도 `0.00`이 아니라 빈 칸

쉬운 예:

- 예전: web route 실패 -> web score 보류, 그러나 official merge -> `merged_score=66`, Stage2처럼 보임
- 지금: web route 실패 -> merged도 보류, raw merged 66점은 참고값으로만 남음

## 2026-06-12 추가 보강: 리포트/리플레이 출력 점수 일원화

문제 가능성:

- core runner는 invalid score를 `score_total=null`로 막아도, 백테스트/리플레이/문서 렌더러가 `score.total_score`를 직접 쓰면 raw 0점 또는 raw 참고점수가 다시 최종점수처럼 보일 수 있다.
- 특히 "아까는 80점대, 지금은 60점대"처럼 보이는 혼동은 대부분 정상 점수와 raw/pending 점수가 같은 칼럼명으로 섞일 때 생긴다.

추가 불변식:

- 사용자-facing 점수 칼럼은 `visible_score_total(score)`만 사용한다.
- invalid score는 JSON에서 `null`, CSV/Markdown에서 빈 칸으로 표시한다.
- raw 참고값은 `raw_score_total_before_*_block` 또는 `raw_score_before_block` 이름으로만 노출한다.
- invalid score 후보는 랭킹에서 점수 후보 뒤로 보낸다.
- `promotion_band()`와 stage gate diagnostics는 invalid score를 `Stage 1`로 해석하지 않고 `Score Pending`으로 표시한다.

적용 경로:

- `historical_case_replay`: invalid total score는 Markdown/JSON 점수에서 빈 값/null
- `historical_universe_replay`: candidate/stage/dropped row의 `total_score`가 `float | None`, 정렬은 `None` 후순위
- `monthly_replay_suite`: top candidate/best candidate 정렬에서 `None` 후순위
- `e2r_standard_replay`: fixture proxy 정렬도 `None` 후순위
- `korea_live_lite`: targeted smoke row는 `ScoreSnapshot`의 `score_valid`를 최종 기준으로 사용
- `stage_gate_diagnostics`: invalid score는 `failed_score_validity`, `Score Pending`

쉬운 예:

- 정상 점수: `score_valid=true`, `score_total=80.1`, `stage=3-Yellow`
- 보류 점수: `score_valid=false`, `score_total=null`, `raw_score_total_before_score_gap_block=68.9`

따라서 이제 "68.9점 Stage2"처럼 말하면 안 된다. 정확한 표현은 "raw 참고값은 68.9지만, score-gap이 해결되지 않아 최종 점수는 보류"다.

추가 검증:

- `PYTHONPATH=src python -m unittest tests.test_korea_live_lite tests.test_stage_gate_diagnostics tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_e2r_standard_flow tests.test_blind_discovery_replay tests.test_asof_research_replay tests.test_asof_evidence_bundle -v`
- 결과: 82 tests passed
- `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,765 tests passed
- `PYTHONPATH=src python -m compileall -q src tests`
- `git diff --check`

## 2026-06-12 추가 보강: 점수 급변처럼 보이는 출력 혼선 제거

사용자 관점의 문제:

```text
방금은 80점대였는데, 이번 출력은 60점대 또는 빈 점수로 보인다.
```

실제 원인은 보통 세 가지가 섞여 보인 것이다.

1. `raw score`
   - deterministic scorer가 일단 계산한 중간 점수.
   - 예: `raw_score_before_block=83`.
2. `visible score`
   - route/score gap/as-of web 검증까지 끝난 뒤 운영에 보여도 되는 점수.
   - 검증이 막히면 `score=null`이어야 한다.
3. `web-only score`와 `merged score`
   - web 연구 단독 점수와 공식/스냅샷 증거까지 합친 점수.
   - 둘을 같은 `score`처럼 보여주면 급변처럼 보인다.

쉬운 예:

```text
run A: raw score 83
run B: visible score null, reason=score_gap_unresolved
```

이건 “83점에서 0점으로 급락”이 아니다.
“83점짜리 계산은 있었지만, 점수 gap 확장이 끝나지 않아서 운영 점수로 확정하지 않았다”는 뜻이다.

이번 보강:

- Blind discovery 최종 후보 `DiscoveredCandidate`에 `score_valid`, `score_blocked_reason`, `score_fingerprint`, `score_variability_drivers`를 추가했다.
- Blind discovery CSV/JSON도 위 필드를 출력한다.
- Historical case replay 결과 row에 score state 필드를 추가했다.
- Historical universe replay의 candidate, dropped candidate, stage snapshot 모두 score state 필드를 보존한다.
- Monthly replay suite top Stage 3 candidate card에 `score_state` 줄을 추가했다.

예상 출력:

```text
score=
score_valid=False
score_blocked_reason=score_gap_unresolved
score_fingerprint=blocked-fingerprint
score_variability_drivers=score_invalid:score_gap_unresolved|raw_score_before_block:83
```

이제 위 상태는 “점수가 낮다”가 아니라 “점수 산출 보류, raw 참고값 83”으로 읽어야 한다.

추가 검증:

- `tests.test_blind_discovery_replay.BlindDiscoveryReplayTests.test_invalid_score_candidate_is_sorted_last_and_written_blank`
- `tests.test_historical_case_replay.HistoricalCaseReplayTests.test_replay_records_stage_backtest_and_layer1_for_each_case`
- `tests.test_historical_universe_replay.HistoricalUniverseReplayTests.test_case_fixture_mode_detects_known_structural_winners`
- `tests.test_monthly_replay_suite.MonthlyReplaySuiteTests.test_top_stage3_cards_do_not_fallback_to_diagnostics_when_score_pending`

최종 재검증:

- 관련 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 87 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,774 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: block flag 불일치 방어

문제 가능성:

- 어떤 코드가 `score_blocked_by_score_gap=100` 같은 block flag를 넣었는데 실수로 `score_valid=0`을 빠뜨릴 수 있다.
- 예전 helper는 `score_valid`가 없으면 기본 valid로 봤기 때문에, 이런 불일치 snapshot이 다시 정상 점수처럼 살아날 수 있었다.

추가 불변식:

- `score_blocked_by_theme_route`, `score_blocked_by_score_gap`, `score_blocked_by_asof_web` 중 하나라도 0보다 크면 invalid
- `raw_score_total_before_*_block` key가 있으면 invalid
- StageClassifier도 `score_valid` 숫자만 직접 보지 않고 `is_score_valid()` helper를 사용

쉬운 예:

```text
score_valid 없음
score_blocked_by_score_gap=100
raw_score_total_before_score_gap_block=83
```

이제 위 상태는 `83점`이 아니라 `Score Pending / score_gap_unresolved`다. 회사 이벤트가 강해도 Stage 2/3으로 승격되지 않고 Stage 0으로 고정된다.

추가 검증:

- `tests.test_score_validity`
- `tests.test_staging.StageClassifierTests.test_block_flag_without_score_valid_still_cannot_be_promoted`
- `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,765 tests passed

## 2026-06-12 추가 보강: raw block key 기반 reason 추론

문제 가능성:

- block flag 없이 `raw_score_total_before_theme_route_block` 같은 raw key만 남으면 invalid 처리는 되지만 reason이 `score_invalid`로 뭉개질 수 있다.
- 운영자가 보면 "왜 보류인지"가 다시 애매해져서 raw 점수를 정상 점수처럼 해석할 수 있다.

추가 불변식:

- `raw_score_total_before_theme_route_block`만 있어도 `theme_route_unresolved`
- `raw_score_total_before_score_gap_block`만 있어도 `score_gap_unresolved`
- `raw_score_total_before_asof_web_block`만 있어도 `asof_web_score_unresolved`

쉬운 예:

```text
raw_score_total_before_theme_route_block=72
score_valid 없음
score_blocked_by_theme_route 없음
```

이제 위 상태는 generic `score_invalid`가 아니라 `theme_route_unresolved`다. 즉 "72점"이 아니라 "theme route가 확정되지 않은 raw 72 참고값"으로 표시된다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_raw_block_key_invalidates_and_preserves_specific_reason_when_block_flag_is_missing`
- `tests.test_score_validity.ScoreValidityTests.test_score_gap_raw_block_key_preserves_score_gap_reason`
- `tests.test_score_validity.ScoreValidityTests.test_asof_raw_block_key_preserves_asof_reason`
- `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,765 tests passed

## 2026-06-12 추가 보강: Stage 0/5 grade 누수 차단

문제 가능성:

- StageClassifier가 invalid score를 Stage 0으로 막아도, `grade` 계산이 raw `total_score`를 보면 `A`나 `B`처럼 보일 수 있다.
- 그러면 운영 화면에서 `stage=0`인데 `grade=A` 같은 모순이 생겨 다시 점수가 살아난 것처럼 보인다.

추가 불변식:

- Stage 0 grade는 항상 `Watch`
- Stage 5 grade는 항상 `Archive`
- Stage 4B/4C와 Stage 1~3의 기존 등급 로직은 유지

쉬운 예:

```text
stage=0
raw_score_total_before_score_gap_block=83
```

이제 위 상태의 grade는 `A`가 아니라 `Watch`다. `83`은 raw 참고값일 뿐 최종 등급에 쓰이지 않는다.

추가 검증:

- `tests.test_staging.StageClassifierTests.test_block_flag_without_score_valid_still_cannot_be_promoted`
- `tests.test_staging.StageClassifierTests.test_archive_stage_uses_archive_grade_not_raw_score_grade`
- `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,765 tests passed

## 2026-06-12 추가 보강: Daily scan JSON score 표시 안전화

문제 가능성:

- `company_results`는 visible score를 쓰더라도, 같은 JSON 안의 `scores` 배열이 원본 `ScoreSnapshot`을 그대로 직렬화하면 invalid score의 component 0점들이 최종 점수처럼 보일 수 있다.
- 예를 들어 score-gap block으로 raw 83 참고값이 있는 케이스가 `total_score=0`, component 0점 배열로 보이면 "0점 급락"처럼 오해할 수 있다.

추가 불변식:

- Daily scan JSON의 `scores`는 표시용 row로 직렬화한다.
- invalid score는 `total_score=null`
- invalid score는 `component_scores=null`
- raw 참고값은 `raw_score_before_block`에만 보관한다.
- `diagnostic_scores`는 남기되, 표시 점수와 raw 참고값 이름을 분리한다.

쉬운 예:

```json
{
  "score_valid": false,
  "score_blocked_reason": "score_gap_unresolved",
  "total_score": null,
  "raw_score_before_block": 83.0,
  "component_scores": null
}
```

이제 Daily scan JSON에서도 `0점`이나 `83점`이 최종 점수처럼 보이지 않는다.

추가 검증:

- `tests.test_daily_scan.DailyScanRunnerTests.test_score_output_row_hides_invalid_component_scores_and_keeps_raw_reference`
- `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,765 tests passed

## 2026-06-12 추가 보강: invalid component 표시 차단

문제 가능성:

- 총점은 `null`로 막았더라도 component가 그대로 보이면 사용자가 그 component를 최종 채점으로 오해할 수 있다.
- 예를 들어 `score_valid=false`, `raw_score_total_before_score_gap_block=77`인데 `score_components`에 EPS/FCF 16, 가시성 14가 보이면 "총점만 숨겼고 실제 점수는 살아있다"처럼 보인다.

추가 불변식:

- invalid score의 사용자-facing component는 숨긴다.
- 운영 targeted smoke row:
  - `score_total=null`
  - `score_components=null`
  - raw component는 `raw_score_components_before_block`에만 둔다.
- as-of autopsy:
  - `current_score=null`
  - component CSV/Markdown 값은 빈 값
  - 설명은 `Score pending: <reason>`으로 표시
- historical/monthly replay:
  - invalid score의 `score_components`는 빈 dict
  - monthly top card는 diagnostic fallback을 쓰지 않고 `n/a`로 표시

쉬운 예:

```json
{
  "score_valid": false,
  "score_total": null,
  "score_components": null,
  "raw_score_before_block": 77.0,
  "raw_score_components_before_block": {
    "eps_fcf_explosion_score": 16.0
  }
}
```

이제 위 상태는 "77점" 또는 "EPS/FCF 16점"이 아니라 "최종점수 보류, raw 참고값 77"로만 읽힌다.

추가 검증:

- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_targeted_smoke_hides_invalid_score_components`
- `tests.test_asof_stage_promotion_autopsy.AsOfStagePromotionAutopsyTests.test_autopsy_row_hides_components_for_invalid_score`
- `tests.test_monthly_replay_suite.MonthlyReplaySuiteTests.test_top_stage3_cards_do_not_fallback_to_diagnostics_when_score_pending`
- `PYTHONPATH=src python -m unittest tests.test_monthly_replay_suite tests.test_korea_live_lite tests.test_asof_stage_promotion_autopsy tests.test_historical_universe_replay -v`
- 결과: 56 tests passed

## 2026-06-12 추가 보강: 검색 rank 동점 안정성

문제 가능성:

- 같은 검색 결과 세트라도 provider가 결과 순서를 다르게 주면, ranker 동점 후보의 순서가 바뀔 수 있다.
- 그 결과 선택되는 문서가 달라지고, 같은 종목을 다시 돌렸을 때 점수 입력 증거가 달라져 점수가 급변해 보일 수 있다.

추가 불변식:

- SearchResultRanker 정렬 key에 `source`, `url`을 추가했다.
- 같은 score, rank, title인 결과도 URL 기준으로 안정 정렬한다.
- 같은 결과 세트라면 provider 응답 순서가 달라도 ranked order가 같다.

쉬운 예:

```text
입력 A: b.pdf, a.pdf
입력 B: a.pdf, b.pdf
```

이제 두 입력 모두 `a.pdf -> b.pdf` 순서로 정렬된다.

추가 검증:

- `tests.test_web_research_runner.WebResearchRunnerTests.test_ranker_tie_breaks_by_url_not_provider_order`
- `PYTHONPATH=src python -m unittest tests.test_web_research_runner tests.test_monthly_replay_suite tests.test_korea_live_lite tests.test_asof_stage_promotion_autopsy -v`
- 결과: 87 tests passed

## 2026-06-12 최종 검증

이번 문서 기준 추가 보강 후 전체 테스트:

- `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,769 tests passed

정적 검증:

- `PYTHONPATH=src python -m compileall -q src tests`
- `git diff --check`
- 결과: 통과

## 2026-06-12 추가 보강: 독립 증거 가족 부족도 material score-gap 처리

문제 가능성:

- selected EPS/FCF/revision source가 비었을 때는 보류되지만, 독립 증거 가족 자체가 부족한 경우는 낮은 점수처럼 남을 수 있다.
- 예를 들어 가격과 뉴스 조각은 있는데 research report, consensus revision, disclosure 같은 독립 축이 부족하고 LLM도 새 검색을 못 만들면, 이것은 "실제로 낮은 점수"가 아니라 "증거 확장 실패"에 가깝다.

추가 material gap:

- `missing independent evidence families`
- `stage2 non-price bridge`
- `stage3 green cross-evidence gate failed`
- `price-only blowoff guard`
- `theme overheat guard`

쉬운 예:

```text
missing independent evidence families: research_report, consensus_revision
LLM suggested_queries 없음
```

이제 위 상태는 낮은 점수 확정이 아니라 `score_gap_llm_no_suggested_queries`로 보류된다.

추가 검증:

- `tests.test_free_web_research_runner.FreeWebResearchRunnerTests.test_independent_evidence_family_gap_is_material_when_llm_cannot_expand`
- `PYTHONPATH=src python -m unittest tests.test_free_web_research_runner tests.test_score_validity tests.test_stage_gate_diagnostics tests.test_korea_live_lite -v`
- 결과: 93 tests passed

## 2026-06-12 추가 보강: score fingerprint

문제 가능성:

- 같은 종목을 다시 돌렸을 때 점수가 바뀌면, 점수 계산식이 바뀐 것인지 입력 증거/진단 세트가 바뀐 것인지 즉시 구분하기 어렵다.
- 이 구분이 안 되면 "아까 80점대였는데 왜 지금 60점대냐" 같은 문제를 추적하기 어렵다.

추가 불변식:

- `score_fingerprint`를 생성한다.
- fingerprint 입력:
  - symbol
  - as_of_date
  - scoring_version
  - evidence_ids
  - diagnostic_scores
  - component_scores
- evidence/diagnostic 순서만 바뀌면 fingerprint는 같다.
- evidence나 component가 바뀌면 fingerprint도 바뀐다.
- Daily scan score row와 Korea live targeted smoke row에 `score_fingerprint`를 출력한다.
- Targeted smoke row에는 `score_evidence_ids`도 함께 출력한다.

쉬운 예:

```text
1차 실행 score_fingerprint = abc123
2차 실행 score_fingerprint = abc123
```

이 경우 같은 score snapshot으로 판단한 것이다.

```text
1차 실행 score_fingerprint = abc123
2차 실행 score_fingerprint = def456
```

이 경우 점수 계산식보다 먼저 "검색/파싱/증거 세트가 달라졌는지"를 확인해야 한다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_score_fingerprint_is_stable_and_changes_when_evidence_changes`
- `tests.test_daily_scan.DailyScanRunnerTests.test_score_output_row_hides_invalid_component_scores_and_keeps_raw_reference`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_targeted_smoke_hides_invalid_score_components`
- `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_daily_scan tests.test_korea_live_lite tests.test_free_web_research_runner -v`
- 결과: 97 tests passed

## 2026-06-12 추가 보강: score variability drivers

문제 가능성:

- 운영형 재실행 산출물에 `score_total` 숫자만 있으면, 80점대와 60점대가 같은 의미처럼 보인다.
- 실제로 확인한 이전 run log에서는 `theme_rebalance_status=provider_error`인데도 `score_total=60.8265`가 그대로 보였다.
- 이 숫자는 확정 점수가 아니라 LLM 라우팅 실패 상태의 raw 계산값이었다.

이번 보강:

- Korea live targeted smoke row에 `score_variability_drivers`를 추가했다.
- invalid score면 `score_invalid:<reason>`을 반드시 남긴다.
- provider/route/evidence gate 상태가 불안정하면 상태 코드를 남긴다.
- FCF, revision, OP source가 비어 있으면 `estimate_source_missing:*`를 남긴다.
- research report, consensus, consensus revision, agent extracted fields가 비어 있으면 `input_missing:*`를 남긴다.
- post-score-gap 확장이 실행되지 않았거나 막혔으면 `score_gap_expansion_status:*` 또는 `score_gap_blocked:*`를 남긴다.
- review CLI도 targeted score states에 `visible_score`, valid, reason, fingerprint, input_fingerprint, drivers를 같이 보여준다.

쉬운 예:

```text
예전 표시:
SK하이닉스 score_total=60.8265, stage=3-Red
```

이제 같은 상태는 아래처럼 보여야 한다.

```text
visible_score=null
score_total=null
score_valid=false
score_blocked_reason=theme_route_provider_error
research_input_fingerprint=...
score_variability_drivers=[
  "score_invalid:theme_route_provider_error",
  "theme_rebalance_status:provider_error",
  "theme_route_status:provider_error"
]
```

반대로 유효 점수가 68점처럼 낮게 나오면 아래처럼 입력 차이를 같이 보여준다.

```text
score_valid=true
visible_score=68.9
score_total=68.9
research_input_fingerprint=...
score_variability_drivers=[
  "estimate_source_missing:fcf",
  "estimate_source_missing:revision",
  "llm_expansion_query_count:0",
  "score_gap_expansion_status:not_attempted"
]
```

이 경우는 "계산기가 갑자기 80점을 68점으로 바꿨다"가 아니다. 같은 as-of라도 deep 확장, 리포트/컨센서스 구조화, FCF/revision source가 달라진 것이다.

추가 검증:

- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_targeted_smoke_marks_score_invalid_when_theme_route_provider_errors`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_targeted_smoke_hides_invalid_score_components`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_targeted_smoke_explains_valid_score_variability_inputs`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_renders_targeted_score_state_drivers`
- `PYTHONPATH=src python -m unittest tests.test_korea_live_lite tests.test_score_validity tests.test_daily_scan -v`
- 결과: 54 tests passed

## 2026-06-12 추가 보강: 공통 driver와 daily/replay 출력 확장

문제 가능성:

- `score_variability_drivers`가 Korea live targeted smoke에만 있으면, daily scan JSON이나 replay/backtest JSON에서는 다시 숫자만 보일 수 있다.
- 그러면 같은 문제가 다른 화면에서 반복된다.

이번 보강:

- `src/e2r/score_validity.py`에 공통 `score_variability_drivers()` helper를 추가했다.
- Korea live targeted smoke는 로컬 중복 로직 대신 공통 helper를 호출한다.
- Daily scan JSON의 `scores[]`, `company_results[]`에 `score_variability_drivers`를 추가했다.
- Daily `company_results[]`에는 `score_fingerprint`, `feature_input_counts`도 같이 노출한다.
- As-of replay 후보 JSON/CSV에 merged score 기준 `score_valid`, `score_blocked_reason`, `score_fingerprint`, `score_variability_drivers`를 추가했다.
- As-of replay에는 web-only score 기준 `web_only_score_*` 필드도 추가했다.
- E2R standard replay 후보에는 `score_valid`, `score_blocked_reason`, `score_fingerprint`, `score_variability_drivers`를 추가했다.

쉬운 예:

```text
daily scan score=68.9
drivers=estimate_source_missing:fcf|estimate_source_missing:revision
```

이 경우 “점수가 급락했다”가 아니라 “이번 run에서 FCF/revision source가 score input으로 안 들어왔다”는 뜻이다.

```text
as-of replay web_only_score=null
web_only_score_variability_drivers=score_invalid:theme_route_provider_error
merged_score=null
score_variability_drivers=score_invalid:asof_web_score_unresolved
```

이 경우 web-only가 실패했기 때문에 merged score도 보류된 것이다. 낮은 점수 확정이 아니다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_score_variability_drivers_explain_invalid_and_missing_inputs`
- `tests.test_daily_scan.DailyScanRunnerTests.test_daily_runner_scans_historical_fixture_universe_and_writes_outputs`
- `tests.test_daily_scan.DailyScanRunnerTests.test_score_output_row_hides_invalid_component_scores_and_keeps_raw_reference`
- `tests.test_asof_research_replay.AsOfResearchReplayTests.test_outputs_are_written_with_failure_stage_report`
- `tests.test_blind_discovery_replay.BlindDiscoveryReplayTests.test_blind_discovery_runs_and_applies_labels_after_outputs`
- `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay -v`
- 결과: 70 tests passed

## 2026-06-12 최신 최종 검증

최신 보강까지 포함한 전체 테스트:

- `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,774 tests passed

정적 검증:

- `PYTHONPATH=src python -m compileall -q src tests`
- `git diff --check`
- 결과: 통과

## 2026-06-12 추가 보강: 재발 방지 score output contract

문제 가능성:

- 지금 출력 경로를 고쳐도, 나중에 새 JSON/CSV/Markdown 출력에서 `score`만 단독으로 다시 넣을 수 있다.
- 그러면 다시 "아까는 80점대였는데 이번에는 60점대"처럼 보이는 혼선이 재발한다.

이번 보강:

- `tests/test_score_output_contract.py`를 추가했다.
- 핵심 replay 후보 dataclass는 `score` 또는 `total_score`와 함께 아래 필드를 반드시 가져야 한다.
  - `score_valid`
  - `score_blocked_reason`
  - `score_fingerprint`
  - `score_variability_drivers`
- daily/korea/monthly/review 출력은 score state 관련 토큰을 반드시 포함해야 한다.
- E2R standard replay의 fixture proxy 경로도 historical replay에서 온 score state를 잃지 않게 연결했다.
- E2R standard replay candidate driver에 web result의 route diagnostics, feature input counts, expansion query count, scoring archetype을 연결했다.

쉬운 예:

```text
score=65
score_valid=True
score_variability_drivers=
  estimate_source_missing:fcf
  input_missing:research_report
  input_missing:consensus
  llm_expansion_query_count:0
```

이 경우는 "점수가 갑자기 낮아졌다"가 아니라 "이번 후보 점수에는 리포트/컨센서스/LLM 확장 입력이 비어 있었다"로 해석한다.

추가 검증:

- `tests.test_score_output_contract.ScoreOutputContractTests.test_replay_score_output_dataclasses_carry_score_state`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_critical_json_and_markdown_outputs_do_not_emit_score_without_state`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_standard_replay_candidate_drivers_include_input_and_expansion_state`
- `tests.test_blind_discovery_replay.BlindDiscoveryReplayTests.test_fixture_proxy_is_explicit_and_labeled_diagnostic`

최신 재검증:

- 관련 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 90 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,777 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: 80점대/60점대처럼 보이는 run 간 급변 설명

문제 가능성:

- 같은 종목을 다시 돌렸는데 한쪽에서는 80점대, 다른 쪽에서는 60점대처럼 보일 수 있다.
- 실제 원인은 세 가지가 섞일 수 있다.
  - raw 참고 점수와 valid 최종 점수가 같은 `score`처럼 보임
  - live 검색/리포트/컨센서스 입력 수가 run마다 달라짐
  - LLM route가 다른 아키타입 또는 다른 증거 게이트 상태를 만들었음

쉬운 예:

```text
1차 run
score_valid=false
raw_score_before_block=83
score_total=null

2차 run
score_valid=true
score_total=65
```

이건 "83점이 65점으로 급락"이 아니다. 1차의 83은 score-gap을 통과하지 못한 참고 raw 값이고, 2차의 65는 valid로 통과한 실제 표시 점수다. 은행 잔고와 장바구니 예상 합계를 같은 돈처럼 비교하면 안 되는 것과 같다.

이번 보강:

- `score_variability_drivers()`가 valid 점수에도 아래 상태를 남긴다.
  - `score_components:...total=65`
  - `route_state:rebalance=...|route=...|gate=...|route_archetype=...|scoring_archetype=...`
  - `input_count:research_report=...`
  - `input_count:consensus=...`
  - `input_count:consensus_revision=...`
  - `input_count:news_item=...`
  - `evidence_count=...`
  - `score_evidence_count=...`
  - `llm_expansion_query_count=...`

해석 규칙:

```text
score_fingerprint 같음 + score_total 같음
=> 같은 score snapshot이다.

score_fingerprint 다름 + route_state 다름
=> LLM route/archetype 판단 또는 route evidence gate가 달라진 것이다.

score_fingerprint 다름 + input_count 다름
=> 들어온 리포트/컨센서스/뉴스/공시 수가 달라져서 점수 입력 자체가 다르다.

score_valid=false + raw_score_before_block 있음
=> 확정 점수가 아니라 보류 전 참고값이다. stage 판단 점수로 쓰면 안 된다.
```

운영자가 봐야 하는 출력 예:

```text
score_valid=true
score_total=65
score_fingerprint=abc123
score_variability_drivers=[
  "score_components:eps_fcf=20,visibility=10,bottleneck=12,mispricing=8,valuation=9,capital=2,confidence=4,risk=0,total=65",
  "route_state:rebalance=completed|route=transition_detected|gate=source_backed|sector=R2_AI_SEMICONDUCTOR_ELECTRONICS|route_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY|scoring_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "input_count:research_report=2",
  "input_count:consensus=1",
  "evidence_count:9",
  "score_evidence_count:4",
  "llm_expansion_query_count:6"
]
```

이제 같은 종목이 다시 60점대로 보이면 아래처럼 바로 원인 분리가 가능하다.

- `score_components`가 낮음: 어느 항목이 깎였는지 확인한다.
- `route_state`가 다름: LLM route/archetype 전환 판단이 달라졌는지 확인한다.
- `input_count`가 다름: 이번 run에 리포트/컨센서스/뉴스/공시가 덜 들어왔는지 확인한다.
- `score_valid=false`: 점수가 아니라 보류 상태이므로 raw 참고값과 최종 점수를 섞어 비교하지 않는다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_score_variability_drivers_explain_valid_run_state`
- `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite -v`
- 결과: 59 tests passed

최신 재검증:

- 관련 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 91 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,778 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: bare score Markdown 헤더 금지

추가로 확인한 문제 가능성:

- JSON/CSV에 `score_valid`가 있어도, Markdown 표의 헤더가 그냥 `score`면 운영자가 그 숫자를 최종점수로 오해할 수 있다.
- 특히 replay/summary Markdown은 사람이 먼저 보는 파일이라, 헤더 수준에서 점수 의미가 분리되어야 한다.

이번 보강:

- Historical case replay Markdown의 `score` 헤더를 `visible_score`로 바꾸고 `score state` 컬럼을 추가했다.
- Historical universe top Stage 3 Markdown의 `score` 헤더를 `visible_score`로 바꾸고 `score state` 컬럼을 추가했다.
- 후보 없음 행의 `0.0` 표시를 빈 visible score로 바꿨다. 후보 없음은 0점이 아니다.
- `tests/test_score_output_contract.py`에 `test_markdown_tables_do_not_use_bare_score_header`를 추가했다.

허용되는 헤더:

```text
visible_score
cheap_scan_score
score state
score component
```

금지되는 헤더:

```text
score
```

쉬운 예:

```text
나쁜 표:
| case | stage | score |

좋은 표:
| case | stage | visible_score | score state |
```

추가 검증:

- `PYTHONPATH=src python -m unittest tests.test_score_output_contract tests.test_historical_case_replay tests.test_historical_universe_replay -v`
- 결과: 14 tests passed

## 2026-06-12 추가 보강: Markdown/Autopsy/cheap-scan 명칭 혼선 제거

추가로 확인한 문제 가능성:

- daily JSON, targeted smoke JSON, replay CSV에는 score state가 들어갔지만 사람이 바로 보는 Markdown 경로에는 아직 약한 곳이 있었다.
- As-of stage promotion autopsy는 invalid score의 컴포넌트는 숨겼지만 row 자체에 `score_valid`, `score_fingerprint`, `score_variability_drivers`가 없었다.
- Korea live lite calibration Markdown의 near miss 표는 최종 E2R 점수가 아닌 `cheap_scan_total_score`를 보여주면서 컬럼명이 `score`였다.

이번 보강:

- Morning Brief score line에 `상태 valid fp ...` 또는 `상태 pending fp ...`를 추가했다.
- pending score는 계속 `점수 산출 보류`와 `참고 raw`로만 표시한다. `총점 0.0`으로 보이지 않는다.
- As-of stage promotion autopsy row와 CSV/Markdown에 아래 필드를 추가했다.
  - `score_valid`
  - `score_blocked_reason`
  - `score_fingerprint`
  - `score_variability_drivers`
  - `raw_score_before_block`
- As-of stage promotion autopsy Markdown의 Candidate Gate Matrix에 `score state` 컬럼을 추가했다.
- Korea live lite calibration Markdown의 near miss 컬럼명을 `score`에서 `cheap_scan_score`로 바꿨다.

쉬운 예:

```text
Morning Brief:
총점 65.0 | EPS/FCF ... | 상태 valid fp abc123 / 변동요인 score_evidence_count:4

Autopsy:
score=""
score state="pending asof_web_score_unresolved / raw 82.00 / fp def456"

Cheap scan calibration:
cheap_scan_score=42.00
```

이제 세 숫자는 서로 섞이지 않는다.

- `총점 65.0`: valid E2R 최종 표시 점수
- `raw 82.00`: invalid/pending 전 참고값
- `cheap_scan_score=42.00`: 1차 후보 선별 점수

추가 검증:

- `PYTHONPATH=src python -m unittest tests.test_briefing tests.test_korea_live_lite tests.test_asof_stage_promotion_autopsy tests.test_score_output_contract -v`
- 결과: 52 tests passed

최종 재검증:

- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 111 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,791 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 현재 기준 최종 요약

현재 운영 해석 기준:

- 운영에서 비교하는 점수는 `visible_score`다.
- `raw_score_before_block`는 점수 산출 보류 전 참고값이다.
- 따라서 `raw_score_before_block=82`와 `visible_score=65`를 "82점에서 65점으로 급변"으로 해석하면 안 된다.
- `score_valid=false`인 row는 구형 호환 필드 `score`, `score_total`, `total_score`가 있어도 visible score fallback으로 쓰지 않는다.
- 리뷰 출력도 `serialized_visible_score()`를 통해 같은 규칙으로 표시한다.
- 산출물 row 자체는 `score_state_contract_violations()`로 계약 위반을 검사한다.
- 둘 다 `visible_score`인데 달라졌다면 `research_input_fingerprint`와 `score_fingerprint`를 같이 비교한다.
- 여러 종목 row 묶음은 `compare_score_state_rows()`로 비교한다.
- 같은 symbol이 중복되어도 `005930`, `005930#2`처럼 보존해서 누락/덮어쓰기를 막는다.

추가 예:

```text
score_valid=false
score=82
raw_score_before_block=82
```

이 row는 비교 기준상 `visible_score=pending`이다. `score=82`가 있어도 구형 호환 필드 또는 raw 참고값일 수 있으므로 운영 점수로 비교하지 않는다.

```text
before score_valid=false score=82
after  score_valid=true  visible_score=65
```

이 경우 출력은 "82점에서 65점으로 하락"이 아니라 "before는 pending, after는 65"로 해석한다.

최신 검증:

- 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite tests.test_score_output_contract -v`
- 결과: 70 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 116 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,794 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 최종 재검증: score row 묶음 비교 반영 후

최종 상태:

- 점수 비교는 `visible_score`끼리만 한다.
- `raw_score_before_block`는 보류 전 참고값이며 운영 점수와 직접 비교하지 않는다.
- 단일 row 비교는 `compare_score_states()`가 담당한다.
- 여러 row 묶음 비교는 `compare_score_state_rows()`가 담당한다.
- Korea live review의 `targeted score changes`도 공통 row 비교 helper를 사용한다.
- row가 누락되거나 새로 생기거나 중복되어도 비교 row를 조용히 버리지 않는다.

사용자 질문에 대한 최종 해석:

- "아까는 80점대였는데 이번에는 60점대"라고 보이면 먼저 두 값이 모두 `visible_score`인지 확인한다.
- 하나가 `raw_score_before_block`이면 서로 다른 종류의 숫자를 섞어 본 것이다.
- 둘 다 `visible_score`라면 `research_input_fingerprint`와 `score_fingerprint`를 비교해 원인을 분류한다.

쉬운 예:

```text
raw_score_before_block=82
visible_score=65
```

이건 82점에서 65점으로 계산이 변한 게 아니다. 82는 "보류 전 참고값", 65는 "운영 표시 점수"다.

```text
run A visible_score=82 input_fingerprint=a score_fingerprint=x
run B visible_score=65 input_fingerprint=b score_fingerprint=y
```

이건 검색/증거/route/feature 입력 묶음이 달라진 것이다.

```text
run A visible_score=82 input_fingerprint=a score_fingerprint=x
run B visible_score=65 input_fingerprint=a score_fingerprint=y
```

이건 같은 입력에서 계산 결과가 달라진 것이므로 scoring rule/profile/code 변경을 먼저 봐야 한다.

최신 검증:

- 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite tests.test_score_output_contract -v`
- 결과: 68 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 114 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,794 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: 두 실행 score 변화 자동 분류

추가로 확인한 문제 가능성:

- `visible_score`, `score_fingerprint`, `research_input_fingerprint`를 출력해도 사람이 매번 수동으로 해석하면 실수할 수 있다.
- 특히 `82 -> 65` 같은 변화가 보이면 다시 "점수가 갑자기 급변했다"로 읽을 수 있다.

이번 보강:

- 공통 helper `compare_score_states()`를 추가했다.
- 두 실행의 score state를 넣으면 아래 상태 중 하나로 분류한다.
  - `same_score_snapshot`: 같은 score fingerprint다. 같은 계산 결과다.
  - `input_changed`: research input fingerprint가 다르다. 검색/증거/route/feature 입력 묶음이 달라진 것이다.
  - `scoring_changed_same_input`: 입력 fingerprint는 같은데 score fingerprint가 다르다. scoring rule/profile/code 변경을 먼저 의심해야 한다.
  - `inconsistent_output_same_score_fingerprint`: score fingerprint가 같은데 visible score가 다르다. 출력 alias/직렬화 버그를 의심해야 한다.
  - `fingerprint_missing`: 비교에 필요한 fingerprint가 부족하다. 숫자만 보고 단정하지 않는다.
- daily `component_scores`와 live `score_components`를 둘 다 읽어서 컴포넌트별 변화도 같이 보여준다.
  - 예: `component_delta:earnings_visibility=-8`
  - 예: `component_delta:bottleneck_pricing=-5`
- `score_variability_drivers`의 추가/삭제도 같이 보여준다.
  - 예: `variability_driver_added:estimate_source_missing:revision`
- review CLI에 이전 run 비교 옵션을 추가했다.
  - `--previous-output-directory`
  - `--previous-as-of-date`
- review summary에 `targeted score changes` 줄을 추가했다.

쉬운 예:

```text
이전 run:
visible_score=82
score_fingerprint=score-a
research_input_fingerprint=input-a

현재 run:
visible_score=65
score_fingerprint=score-b
research_input_fingerprint=input-b
```

출력:

```text
change=input_changed before=82 after=65 delta=-17
```

이 경우는 "같은 입력을 계산했는데 점수가 갑자기 바뀐 것"이 아니다. 입력 묶음이 달라진 것이다.

컴포넌트가 같이 들어오면 아래처럼 어느 항목이 깎였는지도 보인다.

```text
drivers=visible_score_delta:-17,component_delta:earnings_visibility=-8,component_delta:bottleneck_pricing=-5
```

즉 "65점으로 낮아졌다"에서 끝나지 않고, 실적가시성/병목가격 쪽이 얼마나 내려갔는지 바로 확인할 수 있다.

반대로:

```text
이전 run:
visible_score=82
score_fingerprint=score-a
research_input_fingerprint=input-a

현재 run:
visible_score=65
score_fingerprint=score-b
research_input_fingerprint=input-a
```

출력:

```text
change=scoring_changed_same_input before=82 after=65 delta=-17
```

이 경우는 같은 입력에서 scoring 결과가 달라진 것이므로 scoring/profile/code 변경을 먼저 확인해야 한다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_classifies_input_changed_score_move`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_classifies_same_input_scoring_change`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_flags_inconsistent_output_when_same_score_fingerprint_moves`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_reports_component_and_driver_changes`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_summary_compares_previous_output_directory`

## 2026-06-12 추가 보강: score row 묶음 비교 공통화

추가로 확인한 문제 가능성:

- 단일 row는 `compare_score_states()`로 비교할 수 있지만, 운영 산출물은 보통 여러 종목 row 묶음이다.
- 각 CLI/파이프라인이 종목 묶음을 제각각 비교하면 어떤 경로에서는 `visible_score`, `score_fingerprint`, `research_input_fingerprint` 비교가 빠질 수 있다.
- 같은 symbol row가 중복되면 dict 변환 과정에서 앞 row가 덮어써져서 "왜 점수가 바뀌었는지"를 추적할 row 자체가 사라질 수 있다.

이번 보강:

- 공통 helper `compare_score_state_rows()`를 추가했다.
- row key는 기본적으로 `symbol`, `case_id`, `company`, `name` 순서로 잡는다.
- key가 없는 row는 `row:0`, `row:1`처럼 위치 기반 key로 보존한다.
- 같은 key가 두 번 나오면 `005930`, `005930#2`처럼 suffix를 붙여 둘 다 보존한다.
- Korea live review의 `targeted score changes`도 이 공통 helper를 사용하게 바꿨다.

쉬운 예:

```text
이전 run:
005930 visible_score=82 input=a score=score-a
009999 visible_score=71 input=old score=old-score

현재 run:
000111 visible_score=69 input=new score=new-score
005930 visible_score=65 input=b score=score-b
```

출력 해석:

```text
000111 change=missing_before_state
005930 change=input_changed before=82 after=65 delta=-17
009999 change=missing_after_state
```

즉 "점수가 갑자기 80점대에서 60점대로 바뀌었다"에서 끝나지 않고:

- `missing_before_state`: 이번 run에 새로 들어온 row다.
- `input_changed`: 같은 종목이지만 검색/증거/route/feature 입력 묶음이 달라졌다.
- `missing_after_state`: 이전에는 있었는데 이번 run에는 빠졌다.

중복 row 예:

```text
이전 run:
005930 visible_score=82
005930 visible_score=77

현재 run:
005930 visible_score=82
```

출력:

```text
005930 change=...
005930#2 change=missing_after_state
```

이렇게 해야 중복 row가 조용히 사라지지 않는다.

사용자 질문에 대한 운영 답:

- 80점대가 `raw_score_before_block`이고 60점대가 `visible_score`이면 서로 다른 점수라서 비교하면 안 된다.
- 둘 다 `visible_score`인데 `research_input_fingerprint`가 다르면 검색/증거/route 입력이 달라진 것이다.
- 둘 다 `visible_score`이고 `research_input_fingerprint`도 같은데 점수가 바뀌면 scoring rule/profile/code 변경을 의심해야 한다.
- `score_fingerprint`가 같은데 `visible_score`가 다르면 출력 alias/직렬화 버그다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_compare_score_state_rows_tracks_missing_and_changed_rows`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_state_rows_keeps_duplicate_keys_visible`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_keeps_missing_targeted_score_rows_visible`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_critical_output_paths_keep_score_state_contracts`

## 2026-06-12 추가 보강: daily/live 출력의 visible_score 계약

추가로 확인한 문제 가능성:

- Daily scan JSON의 `scores[]`는 값은 visible score였지만 필드명이 `total_score`였다.
- Daily scan JSON의 `company_results[]`는 값은 visible score였지만 호환 필드 `score`만 보고 해석할 수 있었다.
- Korea live lite targeted smoke 결과도 `score_total`만 보면 raw/cheap/visible 중 어느 의미인지 다시 헷갈릴 수 있었다.
- Morning brief 문장도 `총점`이라고 쓰면 raw 참고값이나 cheap scan score와 섞어서 읽을 위험이 있었다.

이번 보강:

- Daily scan `scores[]`에 `visible_score`를 추가했다.
- Daily scan `scores[]`에도 가능한 경우 `research_input_fingerprint`를 넣는다.
- Daily scan `company_results[]`에 기존 `score`를 유지하면서 `visible_score`를 추가했다.
- Korea live lite targeted smoke row에 `visible_score`를 추가했다.
- Review CLI targeted score state가 `score_total` 대신 `visible_score`를 우선 표시한다.
- Morning brief 문구를 `총점과 주요 점수`에서 `표시점수와 주요 점수`로 바꿨다.
- Score output contract test에 daily/live의 `"visible_score"` 필수 토큰을 추가했다.

쉬운 예:

```text
기존 daily company_results:
score=65
score_valid=true

새 daily company_results:
score=65
visible_score=65
score_valid=true
research_input_fingerprint=...
```

운영 해석:

- 자동화 호환 때문에 `score`와 `total_score`는 남아 있을 수 있다.
- 사람이 비교할 때는 무조건 `visible_score`를 기준으로 본다.
- 리뷰 CLI도 `visible_score=...` 형식으로 표시한다.
- `score_valid=false`이면 `visible_score=null`이고, raw 참고값은 `raw_score_before_block`만 본다.
- 같은 종목 같은 날짜에서 `visible_score`가 바뀌면 `score_fingerprint`와 `research_input_fingerprint`를 같이 비교한다.

재검증:

- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 111 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,791 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 현재 최종 재검증

현재 문서 기준 최종 상태:

- `score_valid=false`는 visible score가 아니다.
- raw 점수는 `raw_score_before_block` 계열로만 본다.
- 운영 점수 비교는 `visible_score`끼리만 한다.
- `score_fingerprint`로 계산 결과 스냅샷을 비교한다.
- `research_input_fingerprint`로 검색/증거/route/feature 입력 묶음을 비교한다.

최신 검증:

- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 111 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,791 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: research_input_fingerprint

추가로 확인한 문제 가능성:

- `score_fingerprint`는 계산 결과 스냅샷의 신분증이다.
- 하지만 같은 종목을 다시 돌렸을 때 검색 결과, evidence, feature input, LLM route diagnostics가 달라지면 점수도 달라질 수 있다.
- 이 경우에도 숫자만 보면 "모델이 갑자기 80점에서 60점으로 바뀌었다"처럼 보일 수 있다.

이번 보강:

- 공통 helper `research_input_fingerprint()`를 추가했다.
- fingerprint에 다음 입력을 반영한다.
  - score evidence id
  - evidence id/source/title/url/date/parsed field/excerpt digest
  - queries run
  - route diagnostics
  - feature input counts
  - selected source fields
  - search result identity
- Daily scan company result에 `research_input_fingerprint`를 추가했다.
- Korea live lite targeted smoke row에 `research_input_fingerprint`를 추가했다.
- Review CLI targeted score state에 `input_fingerprint=...`를 표시한다.
- As-of replay, Blind discovery, E2R standard replay, Historical case replay, Historical universe replay, Stage promotion autopsy dataclass/output에도 `research_input_fingerprint`를 보존한다.
- `score_variability_drivers`에도 `research_input_fingerprint:<hash>`를 넣는다.

쉬운 예:

```text
run A
visible_score=82
score_fingerprint=aaa
research_input_fingerprint=inp1

run B
visible_score=65
score_fingerprint=bbb
research_input_fingerprint=inp2
```

이 경우는 "계산기가 같은 입력을 다르게 계산했다"가 아니다. 검색/증거/route 입력 묶음이 달라진 것이다.

반대로:

```text
run A
visible_score=82
score_fingerprint=aaa
research_input_fingerprint=inp1

run B
visible_score=65
score_fingerprint=bbb
research_input_fingerprint=inp1
```

이 경우는 같은 입력에서 점수 결과가 달라진 것이므로 scoring rule, profile, stage gate, code version을 먼저 의심해야 한다.

운영 해석 순서:

1. `score_valid=false`면 visible score가 아니다. raw 참고값과 비교하지 않는다.
2. `visible_score`끼리만 비교한다.
3. `score_fingerprint`가 같으면 같은 score snapshot이다.
4. `score_fingerprint`가 다르고 `research_input_fingerprint`도 다르면 입력이 달라진 것이다.
5. `research_input_fingerprint`는 같은데 `score_fingerprint`가 다르면 scoring/profile/code 변경을 의심한다.

추가 검증:

- `tests.test_score_validity.ScoreValidityTests.test_research_input_fingerprint_is_stable_and_changes_with_inputs`
- `tests.test_score_validity.ScoreValidityTests.test_score_variability_drivers_include_input_fingerprint_when_present`
- 관련 replay/backtest dataclass contract에 `research_input_fingerprint` 필수 추가

최신 재검증:

- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 111 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,791 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: replay 후보 산출물 visible_score 별칭

추가로 확인한 문제 가능성:

- Markdown은 `visible_score`로 바뀌었지만 CSV/JSON 후보 산출물에는 기존 호환 필드인 `score`가 남아 있다.
- 값 자체는 이미 visible score지만, 사람이 CSV/JSON을 직접 보면 `score`라는 이름 때문에 raw score나 cheap scan score와 다시 섞어 볼 수 있다.

이번 보강:

- As-of replay `discovered_candidates.csv/json`에 `visible_score`를 추가했다.
- Blind discovery replay `discovered_candidates.csv/json`에 `visible_score`를 추가했다.
- E2R standard replay `jsonable()` 후보 출력에도 `visible_score`를 추가했다.
- 기존 자동화 호환을 위해 기존 `score` 필드는 유지한다. 단, 운영자가 보는 기준 이름은 `visible_score`다.
- Markdown score contract test를 더 엄격하게 바꿨다. 이제 `score state`가 옆에 있어도 헤더 셀이 정확히 `score`면 실패한다.
- As-of stage promotion autopsy Markdown의 `score` 헤더를 `visible_score`로 바꿨다.

쉬운 예:

```text
기존 CSV/JSON:
score=65
score_valid=true

새 CSV/JSON:
score=65
visible_score=65
score_valid=true
```

운영 해석:

- `visible_score`: stage 판단에 써도 되는 표시 점수
- `raw_score_before_block`: 보류 전 참고값
- `cheap_scan_score`: 1차 후보 선별 점수

따라서 앞으로 숫자를 비교할 때는 `visible_score`끼리만 비교한다.

추가 검증:

- `PYTHONPATH=src python -m unittest tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_score_output_contract tests.test_asof_stage_promotion_autopsy -v`
- 결과: 22 tests passed
- Markdown score header 검색: production/backtest/pipeline Markdown renderer에서 bare `score` 헤더 없음

최종 재검증:

- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 111 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,791 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 현재 파일 끝 기준 최종 요약

현재 운영 해석 기준:

- 운영에서 비교하는 점수는 `visible_score`다.
- `raw_score_before_block`는 점수 산출 보류 전 참고값이다.
- 따라서 `raw_score_before_block=82`와 `visible_score=65`를 "82점에서 65점으로 급변"으로 해석하면 안 된다.
- `score_valid=false`인 row는 구형 호환 필드 `score`, `score_total`, `total_score`가 있어도 visible score fallback으로 쓰지 않는다.
- 둘 다 `visible_score`인데 달라졌다면 `research_input_fingerprint`와 `score_fingerprint`를 같이 비교한다.
- 여러 종목 row 묶음은 `compare_score_state_rows()`로 비교한다.
- 같은 symbol이 중복되어도 `005930`, `005930#2`처럼 보존해서 누락/덮어쓰기를 막는다.

추가 예:

```text
score_valid=false
score=82
raw_score_before_block=82
```

이 row는 비교 기준상 `visible_score=pending`이다. `score=82`가 있어도 구형 호환 필드 또는 raw 참고값일 수 있으므로 운영 점수로 비교하지 않는다.

```text
before score_valid=false score=82
after  score_valid=true  visible_score=65
```

이 경우 출력은 "82점에서 65점으로 하락"이 아니라 "before는 pending, after는 65"로 해석한다.

리뷰 출력 예:

```text
targeted score states:
009999 stage=0 visible_score=pending valid=False reason=score_gap_unresolved ...
```

`score_total=82`가 row 안에 남아 있어도 리뷰는 `visible_score=82`로 표시하지 않는다.

row 계약 위반 예:

```text
score_valid=false
visible_score=82
score_total=82
```

이 row는 아래 위반으로 잡힌다.

```text
invalid_visible_score_present
invalid_compat_score_present:score_total
```

valid row인데 `visible_score`가 없거나 valid row에 raw block marker가 남아 있어도 위반으로 잡힌다.

최신 검증:

- 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite -v`
- 결과: 83 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 122 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,802 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: invalid compat score 정규화

사용자가 본 문제:

- "아까는 80점대였는데 이번에는 60점대"처럼 보였다.
- 실제로는 일부 출력에서 `score_valid=false`인데도 구형 호환 필드 `score`, `score_total`, `total_score`가 남아 있을 수 있었다.
- 이 값은 운영 점수가 아니라 block 전 참고값인데, CSV/JSON을 직접 보면 정상 점수처럼 보일 수 있었다.

이번 보강:

- `normalized_score_state_payload()`를 추가했다.
- invalid marker가 있으면 `visible_score`, `score`, `score_total`, `total_score`를 모두 `null`로 정규화한다.
- valid row인데 `score`만 있고 `visible_score`가 없으면 안전한 방식으로 `visible_score`를 채운다.
- E2R standard replay `jsonable()`이 더 이상 invalid `score=83`을 `visible_score=83`으로 복사하지 않는다.
- As-of replay와 blind discovery replay의 CSV/JSON writer도 invalid score를 빈 값/null로 쓴다.
- `score_state_contract_violations()`로 invalid row의 compat score 잔존을 테스트에서 잡는다.

쉬운 예:

```text
기존 위험 출력:
score_valid=false
score=83
raw_score_before_block=83

사람이 보기에는 83점처럼 보일 수 있음.
```

```text
새 출력:
score_valid=false
score=null
visible_score=null
raw_score_before_block=83

운영 해석은 pending이고, 83은 참고값이다.
```

따라서 앞으로 같은 종목을 다시 돌렸을 때:

- `raw_score_before_block=83`과 `visible_score=65`는 "83점에서 65점으로 급락"이 아니다.
- `pending` 상태가 검증 완료 후 `visible_score=65`가 된 것이다.
- 진짜 급변 여부는 두 실행 모두 `visible_score`가 존재할 때만 본다.
- 두 `visible_score`가 다르면 `research_input_fingerprint`와 `score_fingerprint`를 같이 비교한다.

최신 재검증:

- 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_blind_discovery_replay tests.test_asof_research_replay -v`
- 결과: 49 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 127 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,807 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: 표시 점수 별칭까지 invalid 정규화

추가로 확인한 재발 가능성:

- `score`, `score_total`, `total_score`만 막으면 부족하다.
- replay/autopsy 경로에는 `current_score`, `merged_score`, `web_only_score` 같은 별칭도 있다.
- 정상 생성 경로에서는 이미 `visible_score_total()`로 들어가지만, 미래 코드나 수동 row가 invalid 상태에서 별칭 숫자를 넣으면 다시 "80점대였다"처럼 보일 수 있다.

이번 보강:

- 공통 정규화 helper가 `current_score`, `merged_score`도 표시 점수 별칭으로 취급한다.
- invalid row에서 아래 필드가 non-null이면 계약 위반으로 잡는다.
  - `visible_score`
  - `current_score`
  - `merged_score`
  - `score`
  - `score_total`
  - `total_score`
- as-of replay writer는 parent score 기준으로 `score`, `visible_score`, `merged_score`를 정규화한다.
- as-of replay writer는 web-only score 기준으로 `web_only_score`를 별도 정규화한다.
- as-of stage promotion autopsy serializer도 invalid `current_score`를 null로 만든다.
- Morning briefing은 표시 점수를 직접 `score.total_score`에서 읽지 않고 `visible_score_total()`만 쓴다.
- LLM score-gap reason code의 `SCORE_TOTAL` 이름을 `RAW_SCORE_TOTAL_BEFORE_GAP`로 바꿨다.

쉬운 예:

```text
위험한 as-of row:
score_valid=false
score=83
merged_score=83
web_only_score=77
raw_score_before_block=83
```

이전에는 CSV/JSON 일부 칸에 83 또는 77이 남아 운영 점수처럼 보일 수 있었다.

```text
새 as-of row:
score_valid=false
score=null
visible_score=null
merged_score=null
web_only_score=null
raw_score_before_block=83
```

해석은 "83점에서 60점대로 급락"이 아니라 "이전 row는 pending이고 83은 raw 참고값"이다.

최신 재검증:

- 별칭 정규화 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_asof_research_replay tests.test_asof_stage_promotion_autopsy tests.test_score_output_contract -v`
- 결과: 48 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 176 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,811 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: score_valid 없는 숫자-only row 차단

추가로 확인한 재발 가능성:

- 구형 run log나 불완전 serializer가 `score_valid` 없이 `score=82` 또는 `score_total=82`만 남길 수 있다.
- 이 경우 그 82가 정상 운영 점수인지, raw 참고값인지, cheap scan 점수인지 구분할 수 없다.
- 이전 호환 fallback이 너무 관대하면 review CLI가 이 숫자를 visible score처럼 보여줄 수 있다.

이번 보강:

- serialized score state에서 `score_valid=true`가 없으면 숫자-only row를 pending으로 본다.
- `score_valid=false`, `score_blocked_reason`, `raw_score_before_block` 같은 명시 marker가 있으면 그 사유를 우선 표시한다.
- 아무 marker 없이 숫자만 있으면 `score_valid_missing`으로 처리한다.
- `normalized_score_state_payload()`는 이런 ambiguous row의 `score`, `visible_score`, `current_score`를 null로 정리한다.
- review CLI도 이전 run log가 `score_total=82`만 가지고 있으면 `visible_score=pending`으로 표시한다.

쉬운 예:

```text
구형/불완전 row:
score_total=82
```

이제 이 값은 운영 점수로 보지 않는다.

```text
review 표시:
visible_score=pending
drivers=before_visible_score_ignored:score_valid_missing_without_visible_score
```

정상 점수로 보이려면 최소한 아래처럼 상태가 같이 있어야 한다.

```text
score_valid=true
visible_score=82
score_fingerprint=...
research_input_fingerprint=...
```

최신 재검증:

- score-validity 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity -v`
- 결과: 30 tests passed
- review/계약 집중 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite tests.test_score_output_contract -v`
- 결과: 84 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 179 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,814 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: 보조 점수 alias 공통 정규화

추가로 확인한 재발 가능성:

- `score`, `visible_score`, `merged_score`, `current_score`는 공통 정규화를 타고 있었다.
- 하지만 `web_only_score` 같은 보조 점수는 호출부에서 작은 payload를 직접 만들어 정규화하고 있었다.
- 지금은 맞게 동작해도, 다음에 `broker_only_score`, `news_only_score` 같은 보조 컬럼이 생기면 같은 실수를 반복할 수 있다.
- 특히 숫자는 있는데 `score_valid`가 없는 row는 정상 점수인지 raw 참고값인지 알 수 없으므로 운영 점수로 보여주면 안 된다.

이번 보강:

- `src/e2r/score_validity.py`에 `normalized_score_alias_value()`를 추가했다.
- 보조 점수도 `score_valid=true`일 때만 값을 유지한다.
- `score_valid=false`, `score_blocked_reason`, 또는 `score_valid` 누락이면 보조 점수는 `null`/빈 칸으로 정리한다.
- `score_valid=true`와 `score_blocked_reason=score_gap_unresolved`가 동시에 있는 충돌 상태도 보류로 본다.
- as-of replay의 `web_only_score` CSV/JSON 출력이 새 helper를 사용하게 바꿨다.

쉬운 예:

```text
web_only_score=77
web_only_score_valid 없음
web_only_score_blocked_reason 없음
```

이제 이 값은 운영 점수가 아니다.

```text
CSV/JSON 출력:
web_only_score=null
```

정상 점수로 보이려면 아래처럼 상태가 같이 있어야 한다.

```text
web_only_score=77
web_only_score_valid=true
web_only_score_fingerprint=...
web_only_research_input_fingerprint=...
```

사용자 질문에 대한 현재 답:

- "아까는 80점대, 지금은 60점대"처럼 보이면 먼저 두 값이 모두 `visible_score`인지 봐야 한다.
- 80점대가 `raw_score_before_block`, `score_valid_missing` 숫자, 또는 `web_only_score_valid` 없는 보조 숫자이면 최종 점수가 아니다.
- 둘 다 `visible_score`이고 둘 다 `score_valid=true`이면 그때 `research_input_fingerprint`와 `score_fingerprint`로 원인을 분류한다.
- 예: 입력 fingerprint가 다르면 검색/증거/route가 달라진 것이고, 입력 fingerprint는 같은데 score fingerprint만 다르면 scoring rule/profile/code 변화다.

최신 재검증:

- score-validity 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity -v`
- 결과: 31 tests passed
- as-of replay 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_asof_research_replay -v`
- 결과: 10 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 180 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,815 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: ScoreSnapshot도 score_valid 명시 필수

추가로 확인한 재발 가능성:

- serialized row는 `score_valid`가 없으면 pending으로 막고 있었다.
- 하지만 내부 `ScoreSnapshot` 객체는 `score_valid`가 없을 때 기본 valid처럼 볼 여지가 있었다.
- 그러면 어떤 경로가 `ScoreSnapshot(total_score=82)`만 만들고 diagnostics에 `score_valid`를 안 넣어도, 출력 helper가 82를 visible score로 볼 수 있었다.

이번 보강:

- `is_score_valid()`가 더 이상 `score_valid` 누락을 valid로 보지 않는다.
- `DeterministicScorer`가 정상 계산 결과에는 `diagnostic_scores["score_valid"] = 100.0`을 기본으로 넣는다.
- 따라서 정상 scorer 결과는 명시 valid이고, 수동/legacy snapshot에 marker가 없으면 pending이다.
- 정상 의도 테스트 fixture에는 `score_valid=100`을 명시해 "정상 점수"와 "보류 점수"를 분리했다.

쉬운 예:

```text
ScoreSnapshot(total_score=82, diagnostic_scores={})
```

이제 이 값은 표시 가능한 점수가 아니다.

```text
visible_score=null
score_block_reason=score_invalid
stage=0
```

정상 점수는 아래처럼 생성된다.

```text
DeterministicScorer().score(...)
diagnostic_scores["score_valid"] = 100.0
visible_score=total_score
```

운영 해석:

- 80점대 숫자가 있어도 `score_valid`가 없으면 최종 점수가 아니다.
- `score_valid=false`와 `score_valid` 누락은 모두 visible score 비교 대상이 아니다.
- 사람이 비교하는 값은 여전히 `score_valid=true`인 `visible_score`뿐이다.

최신 재검증:

- score/stage/output 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_stage_gate_diagnostics tests.test_staging tests.test_score_output_contract tests.test_scoring -v`
- 결과: 60 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_scoring tests.test_stage_gate_diagnostics tests.test_staging -v`
- 결과: 203 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,816 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: score_valid 숫자/문자 해석 엄격화

추가로 확인한 재발 가능성:

- serialized output에서는 `score_valid`가 bool이 아니라 숫자나 문자열로 들어올 수 있다.
- Python의 느슨한 bool 해석을 쓰면 `-1` 같은 이상값도 참처럼 보일 수 있다.
- 그러면 `score_valid=-1`, `score=82` 같은 row가 표시 가능한 점수처럼 살아나고, 다음 실행의 정상 `visible_score=65`와 섞여 "82점에서 65점으로 급변"처럼 보일 수 있다.

이번 보강:

- `_state_bool()`은 bool, 숫자, 문자열을 명시 규칙으로만 해석한다.
- `score_valid=True`, `1`, `100.0`, `"true"`, `"100.0"`은 valid다.
- `score_valid=False`, `0`, `"0"`, `"0.0"`, `-1`, `"-1"`은 valid가 아니다.
- `"unknown"`처럼 숫자로 해석할 수 없는 문자열은 ambiguous/pending으로 보고 점수를 숨긴다.

쉬운 예:

```text
score=82
score_valid=-1
```

이제 이 값은 최종 점수가 아니다.

```text
visible_score=null
score_state=score_valid_false
```

반대로 정상 점수는 아래처럼 명확해야 한다.

```text
score=65
score_valid=true
visible_score=65
```

운영 해석:

- 점수 비교는 `score_valid=true`인 `visible_score`끼리만 한다.
- `score_valid <= 0`, 누락, 알 수 없는 문자열이면 pending이다.
- 80점대가 pending/raw/legacy 숫자이고 60점대가 valid visible이면, "점수가 급락"이 아니라 "이전 숫자는 최종 점수가 아니었다"로 해석한다.
- 둘 다 valid visible인데도 달라졌다면 `research_input_fingerprint`, `score_fingerprint`, component delta로 원인을 추적한다.

최신 재검증:

- score-validity 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity -v`
- 결과: 33 tests passed
- live/contract 초점 테스트: `PYTHONPATH=src python -m unittest tests.test_korea_live_lite tests.test_score_output_contract -v`
- 결과: 54 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_scoring tests.test_stage_gate_diagnostics tests.test_staging -v`
- 결과: 205 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,817 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 보강: historical JSON visible_score alias

추가로 확인한 재발 가능성:

- historical case/universe/monthly replay JSON은 `total_score` 필드를 가지고 있었다.
- 값 자체는 이미 `visible_score_total()`에서 온 표시 가능 점수였지만, 이름이 `total_score`이면 raw 계산 점수와 다시 헷갈릴 수 있다.
- Markdown은 `visible_score` 헤더를 쓰고 있었지만 JSON 소비자는 `total_score`만 보고 "80점대였다"처럼 해석할 수 있었다.

이번 보강:

- historical case replay `_jsonable()`이 `total_score + score_valid` row를 `normalized_score_state_payload()`로 정규화한다.
- historical universe replay `_jsonable()`도 같은 정규화를 적용한다.
- monthly replay suite `_jsonable()`도 nested historical replay 후보를 같은 규칙으로 정규화한다.
- JSON 결과에 `visible_score` alias가 추가된다.
- invalid/pending row라면 `total_score`와 `visible_score` 모두 null로 정리된다.

쉬운 예:

```text
기존 historical JSON:
total_score=82
score_valid=true
```

이제:

```text
total_score=82
visible_score=82
score_valid=true
score_fingerprint=...
research_input_fingerprint=...
```

보류 row는:

```text
total_score=null
visible_score=null
score_valid=false
score_blocked_reason=score_gap_unresolved
```

운영 해석:

- JSON에서도 사람이 비교할 기준은 `visible_score`다.
- `total_score`는 legacy 호환 필드로 남을 수 있지만, score state 없이 단독 기준으로 쓰지 않는다.
- `score_valid`, `score_fingerprint`, `research_input_fingerprint`가 같이 있어야 점수 변동 원인을 판단할 수 있다.

최신 재검증:

- score output contract: `PYTHONPATH=src python -m unittest tests.test_score_output_contract -v`
- 결과: 6 tests passed
- historical replay 출력 테스트: `PYTHONPATH=src python -m unittest tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 17 tests passed
- 관련 score output 경로 묶음 테스트: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract tests.test_daily_scan tests.test_korea_live_lite tests.test_briefing tests.test_free_web_research_runner tests.test_asof_stage_promotion_autopsy tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_scoring tests.test_stage_gate_diagnostics tests.test_staging -v`
- 결과: 204 tests passed
- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests -v`
- 결과: 3,816 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 최종 확인: 현재 최신 점수 흔들림 해석 기준

현재 최종 기준:

- 운영에서 비교하는 값은 `visible_score` 하나다.
- `score`, `score_total`, `total_score`, `web_only_score`, `raw_score_before_block`는 `score_valid=true`가 확인되지 않으면 최종 점수가 아니다.
- `score_valid`는 `true`, `1`, `100.0`, `"100.0"`처럼 0보다 큰 값만 valid다.
- `score_valid=false`, `0`, `-1`, 누락, `"unknown"`이면 pending 또는 invalid라서 점수를 숨긴다.
- `score_valid=true`여도 `visible_score`, `score`, `score_total`, `total_score`, `current_score`, `merged_score`가 서로 다르면 계약 위반이다.
- 정상 valid row는 모든 score alias를 동일한 `visible_score` 값으로 정규화한다.

사용자 질문에 대한 답:

```text
아까 80점대
이번 60점대
```

이 상황은 이제 아래 순서로 해석한다.

1. 80점대와 60점대가 둘 다 `visible_score`인지 확인한다.
2. 80점대가 raw/pending/legacy 숫자면 급변이 아니라 "최종 점수로 쓰면 안 되는 숫자"다.
3. 둘 다 `visible_score`이고 둘 다 `score_valid=true`이면 그때만 실제 점수 변동이다.
4. 실제 점수 변동이면 `research_input_fingerprint`, `score_fingerprint`, component delta로 원인을 분류한다.

쉬운 예:

```text
run A: score=82, score_valid 없음
run B: visible_score=65, score_valid=true
```

이건 82점에서 65점으로 떨어진 게 아니다. A의 82는 최종 표시 점수가 아니므로 비교 대상이 아니다.

```text
run A: visible_score=82, score_valid=true, research_input_fingerprint=a
run B: visible_score=65, score_valid=true, research_input_fingerprint=b
```

이건 실제 점수 변동이다. 다만 입력 fingerprint가 다르므로 검색/증거/route 입력이 바뀐 케이스다.

```text
run A: visible_score=82, score_valid=true, research_input_fingerprint=a, score_fingerprint=x
run B: visible_score=65, score_valid=true, research_input_fingerprint=a, score_fingerprint=y
```

이건 같은 입력에서 scoring rule/profile/code가 바뀐 케이스로 봐야 한다.

추가로 막은 케이스:

```text
visible_score=65
score=82
score_total=90
total_score=77
score_valid=true
```

예전에는 사람이 `score=82`나 `score_total=90`을 보고 다른 점수처럼 오해할 수 있었다. 이제 정규화 후에는 아래처럼 한 값만 남는다.

```text
visible_score=65
score=65
score_total=65
total_score=65
score_valid=true
```

정규화 전에 이런 충돌이 보이면 `score_state_contract_violations()`가 `valid_score_alias_mismatch:*`로 잡는다.

추가로 막은 우회 경로:

- dataclass row는 `_jsonable()`에서 정규화되고 있었다.
- 하지만 plain dict로 직접 `{score, score_valid}`를 만든 뒤 JSON/CSV로 내보내면 dataclass 정규화를 우회할 수 있었다.
- 이제 운영 출력과 replay 출력의 `_jsonable()` Mapping branch가 `normalized_score_state_mapping_if_present()`를 통과한다.
- 이 helper는 `score_valid`와 score alias가 같이 있을 때만 정규화한다.
- 따라서 `diagnostic_scores={"score_valid": false, "raw_score_total_before_score_gap_block": 82}` 같은 내부 진단 dict에는 불필요한 `visible_score=null`을 추가하지 않는다.

쉬운 예:

```text
plain dict 입력:
{"score": 82, "score_valid": false, "score_blocked_reason": "score_gap_unresolved"}
```

이제 JSON 직렬화 전:

```text
{"score": null, "visible_score": null, "score_valid": false, "score_blocked_reason": "score_gap_unresolved"}
```

최신 재검증:

- 전체 테스트: `PYTHONPATH=src python -m unittest discover -s tests`
- 결과: 3,820 tests passed
- 정적 검증: `PYTHONPATH=src python -m compileall -q src tests`, `git diff --check`
- 결과: pass

## 2026-06-12 추가 확인: 80점대/60점대 급변처럼 보인 이유

사용자가 본 "아까는 80점대였는데 지금은 60점대" 문제는 점수 엔진이 같은 입력에서 아무 이유 없이 흔들린 케이스로 보기 전에, 먼저 출력 계약 위반 가능성을 제거해야 한다.

핵심은 아래 두 숫자가 서로 다른 의미였다는 점이다.

- 80점대: `score`, `score_total`, `raw_score_before_block` 같은 원시/호환/차단 전 숫자일 수 있다.
- 60점대: `score_valid=true` 상태에서 최종 노출 가능한 `visible_score`일 수 있다.

따라서 앞으로 운영자가 비교할 수 있는 값은 `score_valid=true`인 `visible_score`뿐이다.

쉬운 예:

```text
예전 출력:
score=82
merged_score=65
score_valid=true
```

이 상태에서 사람이 `score`를 보면 82점, `merged_score`나 `visible_score`를 보면 65점처럼 보인다. 실제로는 한 종목이 흔들린 게 아니라 서로 다른 별칭이 충돌한 것이다.

수정 후:

```text
score=65
merged_score=65
visible_score=65
score_valid=true
```

이제 valid row에서는 점수 별칭이 서로 다른 값을 가질 수 없다.

또 다른 예:

```text
예전 출력:
score=83
score_valid=false
score_blocked_reason=score_gap_unresolved
```

이 83은 차단 전 임시 숫자라서 최종 점수로 보면 안 된다.

수정 후:

```text
score=
visible_score=
score_valid=false
score_blocked_reason=score_gap_unresolved
```

CSV는 빈 값, JSON은 `null`로 나간다.

추가 테스트:

- `tests.test_score_output_contract.ScoreOutputContractTests.test_asof_candidate_csv_reconciles_score_aliases_to_visible_score`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_blind_candidate_csv_hides_invalid_compat_score`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_output_contract tests.test_score_validity -v`
- 결과: 44 tests passed

## 2026-06-12 추가 방어: visible_score 없는 alias 충돌 차단

위 패치 이후에도 한 가지 애매한 케이스가 남을 수 있었다.

```text
score=82
score_total=90
total_score=82
score_valid=true
visible_score 없음
```

이 경우 과거 방식은 내부 우선순위에 따라 `score_total=90` 같은 값을 최종값처럼 고를 수 있었다. 이건 사용자가 보기에는 "방금 전에는 82였는데 왜 90이냐"로 보인다.

수정 후에는 이런 row를 최종 점수로 만들지 않는다.

```text
score=
score_total=
total_score=
visible_score=
score_valid=false
score_blocked_reason=score_alias_conflict
```

즉, 기준점이 없는 충돌은 점수를 임의 선택하지 않고 차단한다.

허용되는 케이스:

```text
visible_score=65
score=82
score_total=90
score_valid=true
```

이 경우 `visible_score=65`가 명시 최종 기준이므로 출력 전 모든 alias를 65로 맞춘다.

```text
merged_score=65
score=82
score_valid=true
```

이 경우 `merged_score`는 replay 병합 후 최종 score alias로 취급하므로 `visible_score=65`, `score=65`로 맞춘다.

차단되는 케이스:

```text
current_score=82
merged_score=65
score_valid=true
visible_score 없음
```

`current_score`와 `merged_score`가 서로 다르지만 최종 기준 `visible_score`가 없으므로 `score_alias_conflict`로 막는다.

추가로 plain dict 우회도 막았다.

```text
score=82
score_blocked_reason=score_gap_unresolved
score_valid 없음
```

이제 이런 row도 `score_valid=false`, `visible_score=null`, `score=null`로 정규화된다. 단순한 일반 metric `{score: 82}`는 score-state marker가 없으므로 건드리지 않는다.

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_payload_blocks_conflicting_compat_aliases_without_visible_score`
- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_payload_blocks_conflicting_visible_aliases_without_visible_score`
- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_payload_blocks_nonnumeric_valid_score`
- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_mapping_if_present_normalizes_block_markers_without_score_valid`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_score_output_contract -v`
- 결과: 48 tests passed

## 2026-06-12 추가 방어: 과거 산출물 읽기 경로도 alias 충돌 차단

출력 writer에서 충돌을 막아도, 리뷰 CLI가 과거 JSON/CSV 산출물을 직접 읽으면 같은 문제가 다시 생길 수 있다.

위험 예:

```text
과거 run_log.json row:
score=82
score_total=90
score_valid=true
visible_score 없음
```

이전 읽기 경로에서는 `serialized_visible_score()`가 내부 우선순위로 `score_total=90`을 고를 수 있었다. 그러면 새 산출물의 `visible_score=65`와 비교하면서 "90에서 65로 떨어졌다"처럼 보인다.

수정 후 읽기 경로:

```text
serialized_visible_score(row) -> None
review CLI 표시 -> visible_score=pending
comparison status -> visible_score_missing_before
driver -> before_visible_score_ignored:score_alias_conflict_without_visible_score
```

즉, 과거 산출물이 충돌 row라면 82도 90도 최종 점수로 읽지 않는다. 사람이 보는 리뷰 요약에서도 `pending`으로 표시하고, 원인은 `score_alias_conflict`로 남긴다.

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_blocks_conflicting_compat_aliases_without_visible_score`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_blocks_conflicting_visible_aliases_without_visible_score`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_does_not_display_conflicting_valid_aliases_as_visible`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 91 tests passed

## 2026-06-12 추가 방어: pending 점수와 valid/reason 문구 동기화

숫자는 막혔지만 리뷰 문구가 모순될 수 있는 케이스가 남아 있었다.

위험 예:

```text
score=82
score_total=90
score_valid=true
visible_score 없음
```

이전 표시:

```text
visible_score=pending valid=True reason=valid
```

숫자는 pending인데 상태는 valid라고 보여서 운영자가 다시 혼동할 수 있다.

수정 후 표시:

```text
visible_score=pending valid=False reason=score_alias_conflict
```

`serialized_visible_score()`, `serialized_score_valid()`, `serialized_score_block_reason()`이 같은 판정 규칙을 사용한다.

쉬운 예:

```text
score=82, score_valid=true
-> visible_score=82, valid=True, reason=valid

score=82, score_total=90, score_valid=true
-> visible_score=pending, valid=False, reason=score_alias_conflict

score=82, score_valid 없음
-> visible_score=pending, valid=False, reason=score_valid_missing
```

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_serialized_score_valid_and_reason_match_visible_score_contract`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_does_not_display_conflicting_valid_aliases_as_visible`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 92 tests passed

## 2026-06-12 추가 방어: Markdown/월간 리포트 score state 문구 동기화

리뷰 CLI 외에도 사람이 보는 Markdown 리포트에서 같은 모순이 생길 수 있었다.

위험 예:

```text
HistoricalReplayCandidate(
  total_score=None,
  score_valid=True,
  score_blocked_reason=None
)
```

이전 표시:

```text
visible_score n/a
score state: valid=True; reason=none
```

이건 최종 점수는 없는데 valid라고 표시하는 모순이다.

수정 후 표시:

```text
visible_score n/a
score state: valid=False; reason=visible_score_missing
```

적용한 renderer:

- `historical_case_replay._score_state_text()`
- `historical_universe_replay._candidate_score_state_text()`
- `monthly_replay_suite._candidate_score_state()`

추가 테스트:

- `tests.test_historical_case_replay.HistoricalCaseReplayTests.test_markdown_score_state_does_not_show_valid_true_without_visible_score`
- `tests.test_historical_universe_replay.HistoricalUniverseReplayTests.test_markdown_score_state_does_not_show_valid_true_without_visible_score`
- `tests.test_monthly_replay_suite.MonthlyReplaySuiteTests.test_top_stage3_card_score_state_does_not_show_valid_true_without_visible_score`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite -v`
- 결과: 20 tests passed

## 2026-06-12 추가 방어: CSV writer와 보조 점수 상태 동기화

JSON/Markdown은 정규화됐지만 CSV writer에 남은 위험이 있었다.

위험 예:

```text
score=None
score_valid=True
score_blocked_reason=None
```

이전 CSV 가능 출력:

```text
score=
visible_score=
score_valid=True
score_blocked_reason=
```

점수는 비어 있는데 valid가 True라서 엑셀에서 다시 혼동될 수 있다.

수정 후 CSV:

```text
score=
visible_score=
score_valid=False
score_blocked_reason=visible_score_missing
```

적용한 writer:

- `asof_research_replay._write_candidates()`
- `blind_discovery_replay._write_candidates()`

as-of replay의 보조 점수 `web_only_score`도 같은 규칙을 적용했다.

```text
web_only_score=None
web_only_score_valid=True
-> web_only_score=
-> web_only_score_valid=False
-> web_only_score_blocked_reason=visible_score_missing
```

JSON 직렬화에서도 `web_only_score`, `web_only_score_valid`, `web_only_score_blocked_reason`이 같이 정규화된다.

추가 테스트:

- `tests.test_score_output_contract.ScoreOutputContractTests.test_asof_candidate_csv_uses_normalized_validity_when_visible_score_missing`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_blind_candidate_csv_uses_normalized_validity_when_visible_score_missing`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_output_contract tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_score_validity -v`
- 결과: 70 tests passed

## 2026-06-12 추가 방어: Autopsy Markdown score state 동기화

stage promotion autopsy의 CSV는 `_jsonable()`을 거쳐 정규화됐지만, Markdown score state 문구는 dataclass 원본 `score_valid`를 직접 볼 수 있었다.

위험 예:

```text
current_score=None
score_valid=True
score_blocked_reason=None
```

이전 Markdown 가능 출력:

```text
valid / fp scorefp
```

수정 후:

```text
pending visible_score_missing / fp scorefp
```

적용한 renderer:

- `asof_stage_promotion_autopsy._score_state_text()`

추가 테스트:

- `tests.test_asof_stage_promotion_autopsy.AsOfStagePromotionAutopsyTests.test_autopsy_score_state_text_does_not_show_valid_true_without_visible_score`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_asof_stage_promotion_autopsy tests.test_score_validity -v`
- 결과: 48 tests passed

## 2026-06-12 추가 방어: `score_valid=True`와 raw 차단 마커 동시 존재 차단

사용자가 본 "아까는 80점대였는데 지금은 60점대" 혼란은 대부분 서로 다른 종류의 숫자를 비교할 때 생긴다.

대표 예:

```text
raw_score_before_block=82
visible_score=65
score_valid=True
```

이 행은 그대로 두면 사람이 `82점에서 65점으로 급락했다`고 읽을 수 있다. 하지만 `raw_score_before_block=82`는 보류/차단 전 참고값이고, `visible_score=65`는 최종 표시 후보 점수다. 둘이 같이 있으면 같은 점수 라인의 전후 변화가 아니다.

수정한 계약:

- `score_valid=True`라도 `score_blocked_reason`이 있으면 최종 점수로 보지 않는다.
- `score_valid=True`라도 `raw_score_total_before_*_block` 또는 `raw_score_before_block`이 있으면 최종 점수로 보지 않는다.
- 이런 행은 정규화 시 `visible_score=None`, `score_valid=False`, `score_blocked_reason=<raw 차단 사유>`로 바뀐다.
- 계약 검사에서는 `valid_raw_block_marker_present:*`와 `invalid_visible_score_present`를 같이 잡는다.

쉬운 예:

```text
정상 비교 가능:
  이전 visible_score=82, score_valid=True
  현재 visible_score=65, score_valid=True
  => 실제 점수 변화다.

비교 금지:
  이전 raw_score_before_block=82
  현재 visible_score=65
  => 82는 보류 전 참고값이라 "점수 급락"이 아니다.

비교 금지:
  visible_score=65, score_valid=True, raw_score_before_block=82
  => 한 행에 서로 다른 점수 상태가 섞인 계약 위반이다.
```

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_payload_keeps_visible_valid_and_reason_consistent_across_alias_cases`
- `tests.test_score_validity.ScoreValidityTests.test_score_state_contract_violations_flag_valid_rows_missing_visible_score`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity -v`
- 결과: 44 tests passed
- 명령: `PYTHONPATH=src python -m unittest tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_asof_stage_promotion_autopsy tests.test_score_output_contract tests.test_score_validity -v`
- 결과: 152 tests passed

## 2026-06-12 추가 방어: 비교 함수도 effective score state만 사용

이전 추가 방어 후에도 비교 함수 안에는 남은 위험이 있었다.

위험 예:

```text
before:
  score=82
  score_total=90
  score_valid=true

after:
  visible_score=65
  score_valid=true
```

before row는 `score`와 `score_total`이 서로 충돌하므로 실제 표시 가능 점수가 아니다. 그런데 비교 함수가 원본 `score_valid=true`를 그대로 믿으면 `visible_score_missing_before`처럼 애매하게 보일 수 있었다.

수정 후:

- 비교 함수는 원본 `_state_bool(score_valid)`가 아니라 `serialized_score_valid()`를 사용한다.
- 비교 함수는 원본 `score_blocked_reason`이 아니라 `serialized_score_block_reason()`을 사용한다.
- raw marker, block reason, alias conflict가 있으면 effective valid는 `False`다.

쉬운 예:

```text
before:
  score=82
  score_total=90
  score_valid=true
  => effective valid=false, reason=score_alias_conflict

after:
  visible_score=65
  score_valid=true
  => effective valid=true

비교 결과:
  change=score_became_valid
```

이제 이 경우는 `82점에서 65점으로 하락`이 아니다. `이전 row는 점수 계약 위반이라 pending/invalid였고, 현재 row가 처음으로 valid가 된 것`으로 표시한다.

반대 방향도 동일하다.

```text
before:
  visible_score=74
  score_valid=true

after:
  visible_score=null
  score_valid=false
  score_blocked_reason=score_gap_unresolved

비교 결과:
  change=score_became_invalid
```

## 2026-06-12 추가 방어: 새 score output dataclass 정적 계약

앞으로 핵심 산출물 dataclass에 `score`, `total_score`, `current_score`, `merged_score`, `visible_score`, `score_total` 같은 최종 점수 필드가 새로 추가되면 반드시 아래 필드가 같이 있어야 한다.

- `score_valid`
- `score_blocked_reason`
- `score_fingerprint`
- `research_input_fingerprint`
- `score_variability_drivers`

보조 점수인 `web_only_score`가 있으면 아래도 필수다.

- `web_only_score_valid`
- `web_only_score_blocked_reason`
- `web_only_score_fingerprint`
- `web_only_research_input_fingerprint`
- `web_only_score_variability_drivers`

이 규칙은 `tests.test_score_output_contract.ScoreOutputContractTests.test_score_output_dataclasses_with_score_fields_have_state_contract`에서 정적으로 검사한다.

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 93 tests passed
- 명령: `PYTHONPATH=src python -m unittest tests.test_score_output_contract -v`
- 결과: 11 tests passed

## 2026-06-12 추가 방어: legacy/fallback 점수도 계약 위반으로 노출

운영 리뷰에서 아직 남은 혼동 가능성이 있었다.

예:

```text
score=82
score_valid=true
visible_score 없음
```

이 값은 과거 산출물 호환 필드일 뿐이다. 현재 계약상 최종 표시 점수는 명시 `visible_score`, `current_score`, `merged_score` 중 하나가 있어야 한다. 따라서 `serialized_visible_score()`는 `score`, `score_total`, `total_score`만 보고 최종 점수로 승격하지 않는다.

수정 후:

- `compare_score_states()`는 before/after row의 `score_state_contract_violations()`를 driver에 넣는다.
- review CLI의 targeted score state에 `contract=...`를 표시한다.
- 정상 최신 row는 `contract=ok`로 보인다.
- legacy compat-only row나 alias mismatch row는 계약 위반이 그대로 보인다.

쉬운 예:

```text
score=82
score_valid=true
visible_score 없음

리뷰 표시:
  visible_score=pending
  valid=False
  reason=visible_score_missing
  contract=valid_visible_score_missing
```

즉 `score=82`는 더 이상 표시 점수로 읽지 않는다. 이 row는 "82점"이 아니라 "최종 표시 점수 없음"이다.

다른 예:

```text
visible_score=65
score_total=12
score_valid=true

리뷰 표시:
  visible_score=65
  valid=True
  contract=valid_score_alias_mismatch:score_total
```

이 경우도 `12점과 65점 중 어느 게 맞냐`가 아니라, `visible_score=65`가 표시 기준이고 `score_total=12`는 계약 위반으로 남은 alias다. 새 writer는 이런 alias를 저장 전에 `visible_score`와 같은 값으로 정규화해야 한다.

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_blocks_compat_score_without_visible_score`
- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_reports_contract_violations_even_when_visible_score_is_available`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_prefers_visible_score_over_compat_score_total`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_cli_treats_score_without_validity_as_pending`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 97 tests passed

## 2026-06-12 추가 방어: 출력 JSON 전체 score-state 계약 감사

개별 row 표시와 비교는 막았지만, 운영자가 큰 JSON 파일에서 어느 위치가 문제인지 직접 찾기 어려운 문제가 남아 있었다.

수정 후:

- `find_score_state_contract_violations()`를 추가했다.
- JSON/list/dict를 재귀적으로 훑고, score-state 계약 위반 위치를 경로와 함께 반환한다.
- 기본 모드는 검색 랭킹의 `score=0.9` 같은 내부 점수는 오탐하지 않는다.
- review CLI는 후보 row와 targeted smoke row에 대해서는 legacy `score` 단독도 검사한다.

쉬운 예:

```json
{
  "candidates": [
    {
      "symbol": "005930",
      "score": 82,
      "score_valid": true
    }
  ],
  "targeted_smoke_results": [
    {
      "symbol": "009999",
      "visible_score": 65,
      "score_total": 12,
      "score_valid": true
    }
  ]
}
```

리뷰 출력:

```text
score state contract:
  candidates[0]:valid_visible_score_missing
  targeted_smoke_results[0]:valid_score_alias_mismatch:score_total
```

해석:

- `candidates[0]`: `score=82`는 있지만 `visible_score`가 없으므로 최신 최종 점수 계약이 아니다.
- `targeted_smoke_results[0]`: `visible_score=65`가 표시 기준이고, `score_total=12`는 남아 있으면 안 되는 alias mismatch다.

오탐 방어:

```json
{
  "search_results": [
    {"title": "ranked result", "score": 0.92}
  ]
}
```

기본 감사에서는 위 row를 score-state 위반으로 보지 않는다. 검색 랭킹 점수와 E2R 최종 점수는 다른 종류의 숫자이기 때문이다.

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_find_score_state_contract_violations_scans_nested_outputs_without_ranking_score_false_positive`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_review_summary_reports_score_state_contract_findings_with_paths`

추가 focused 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 96 tests passed

## 2026-06-12 추가 방어: compat alias fallback 완전 차단

사용자가 본 혼동:

```text
아까는 80점대였는데 이번에는 60점대라고 보임
```

실제 원인:

- 옛 run log 일부에 `visible_score=null`인데 `score_total=48~68` 같은 compat 숫자가 남아 있었다.
- 기존 `serialized_visible_score()`가 `visible_score`가 없을 때 `score_total`을 fallback으로 읽을 수 있었다.
- 그래서 라우팅 실패, budget 소진, 구버전 출력 숫자가 최종 점수처럼 보였다.

수정 후 핵심 규칙:

- 최종 비교 점수는 `score_valid=true`인 명시 `visible_score`, `current_score`, `merged_score`뿐이다.
- `score`, `score_total`, `total_score`는 표시 점수의 source가 될 수 없다.
- valid row에서 compat alias만 있으면 `visible_score_missing`으로 막는다.
- valid row에서 `visible_score=65`, `score_total=12`처럼 다르면 `visible_score=65`가 표시 기준이고, alias mismatch 계약 위반을 표시한다.

쉬운 예:

```text
옛 row:
  visible_score=null
  score_total=68.9388
  score_valid=true

새 review 표시:
  visible_score=pending
  valid=False
  reason=visible_score_missing
  contract=valid_visible_score_missing
```

이 경우 `68.9388점`이 아니다. 최종 표시 점수가 없는 불완전 row다.

실제 0612 옛 산출물 재확인:

```text
output/live_target_route_block_verify_0612/005930/korea_live_lite
005930 stage=2 visible_score=pending valid=False reason=visible_score_missing contract=valid_visible_score_missing

output/live_target_operational_selected_only_providerfix_000660_2026-06-12/korea_live_lite
000660 stage=3-Red visible_score=pending valid=False reason=score_valid_missing contract=invalid_compat_score_present:score_total
```

추가 구현:

- Korea live-lite `run_log`에 `score_state_contract_findings`를 추가했다.
- 실행 직후 산출물에 legacy compat-only row가 생기면 run_log에 경로와 사유가 남는다.
- review CLI는 run_log에 저장된 finding과 파일 재스캔 finding을 합쳐 보여준다.
- E2R standard replay candidate에 명시 `visible_score` 필드를 추가했다. `score`만 있는 replay 후보가 최종 점수로 승격되지 않게 하기 위해서다.

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_compare_score_states_blocks_compat_score_without_visible_score`
- `tests.test_score_validity.ScoreValidityTests.test_normalized_score_state_payload_blocks_compat_score_without_visible_score`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_live_lite_run_log_contract_audit_catches_legacy_compat_score_rows`
- `tests.test_score_output_contract.ScoreOutputContractTests.test_standard_replay_candidate_drivers_include_input_and_expansion_state`

추가 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 97 tests passed
- 명령: `PYTHONPATH=src python -m unittest tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_asof_stage_promotion_autopsy tests.test_score_output_contract tests.test_score_validity -v`
- 결과: 157 tests passed

## 2026-06-12 추가 방어: visible_score 필드 자체 필수화

이전 보강은 `score_total` 같은 compat 숫자를 최종 점수로 승격하지 못하게 막았다. 하지만 사용자가 지적한 더 근본적인 기준은 다음이다.

> 운영 산출물 row라면 `visible_score` 키 자체가 반드시 있어야 한다.

즉 아래 row는 숫자가 없어도 계약 위반이다.

```text
symbol=000660
stage=0
score_valid=false
score_blocked_reason=theme_route_provider_error
visible_score 키 없음
```

수정 후:

```text
contract=visible_score_field_missing
```

정상 invalid row는 이렇게 명시해야 한다.

```text
symbol=000660
stage=0
visible_score=null
score_valid=false
score_blocked_reason=theme_route_provider_error
```

쉬운 예:

- `visible_score=82`: 최종 표시 점수가 생김
- `visible_score=null`: 최종 표시 점수는 없지만, 실패/보류 상태를 명시함
- `visible_score 키 없음`: 산출물 계약 실패

구현:

- `score_state_output_contract_violations()` 추가
- `find_score_state_contract_violations(..., require_visible_score_field=True)` 옵션 추가
- Korea live-lite run_log 감사와 review CLI에 해당 옵션 연결
- `score_valid/reason`만 있고 score 숫자 키가 없는 output row도 감사 대상에 포함

추가 테스트:

- `tests.test_score_validity.ScoreValidityTests.test_score_state_output_contract_requires_visible_score_field`
- `tests.test_korea_live_lite.KoreaLiveLiteTests.test_live_lite_run_log_contract_audit_requires_visible_score_field`

추가 재검증:

- 명령: `PYTHONPATH=src python -m unittest tests.test_score_validity tests.test_korea_live_lite -v`
- 결과: 99 tests passed
- 명령: `PYTHONPATH=src python -m unittest tests.test_daily_scan tests.test_korea_live_lite tests.test_asof_research_replay tests.test_blind_discovery_replay tests.test_historical_case_replay tests.test_historical_universe_replay tests.test_monthly_replay_suite tests.test_asof_stage_promotion_autopsy tests.test_score_output_contract tests.test_score_validity -v`
- 결과: 159 tests passed
