# E2R V12 Rolling Calibration Goal

작업 위치:

```text
/home/eorb915/projects/stock_agent
```

입력 위치:

```text
docs/round
```

핵심 목표:

```text
v12 연구 MD를 한 번에 ingest하고,
검증된 safe patch와 아키타입별 점수비중을 E2R 2.2 rolling scoring profile에 실제 반영한다.
```

이 작업은 “연구를 쌓아두기만 하는 작업”이 아니다.

```text
새 연구 MD
-> 검증
-> 중복제거
-> Stage 전이 분석
-> apply / hold / block 결정
-> safe patch 생성
-> configs/e2r_scoring_profile_v2_2.yaml 반영
-> configs/e2r_archetype_weight_profile_v2_2.json 반영
-> configs/e2r_scoring_profile_active.yaml을 e2r_2_2로 유지
```

현재 기본 profile:

```text
active_profile: e2r_2_2
rollback_profile: calibrated
```

자세한 시각화 문서는 다음 파일을 먼저 본다.

```text
docs/core/Architecture.md
```

## 표준 명령

v12 연구 배치가 들어오면 이 명령을 실행한다.

```bash
PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
  --md-input-root docs/round \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12
```

이 명령은 다음을 모두 수행해야 한다.

```text
1. v12 MD discovery
2. MD parser
3. trigger row validation
4. dedupe
5. sector/archetype aggregate
6. stage transition summary
7. rolling calibration ledger 생성
8. promotion decision 생성
9. apply_next_patch spec 생성
10. E2R 2.2 rolling profile 생성
11. archetype weight runtime profile 생성
12. active profile을 e2r_2_2로 설정
13. 보고서 생성
```

`run-v12-full`은 감사용이다. active profile을 바꾸지 않는다.

```text
점수체계까지 반영하려면 run-v12-calibration을 쓴다.
```

## 연구가 점수로 바뀌는 기준

v12 row 하나가 바로 점수가 되는 것은 아니다.

반드시 다음 과정을 통과해야 한다.

```text
raw row
-> validated row
-> representative row
-> aggregate metric
-> promotion decision
-> patch spec
-> v2.2 profile
-> archetype weight profile
```

예시:

```text
잘못된 방식:
  C20 K뷰티 row가 하나 나왔으니 모든 소비재 Stage2 기준을 낮춘다.

올바른 방식:
  C20 row들이 검증되고,
  positive와 counterexample 균형이 맞고,
  stage transition이 충분하고,
  apply_next_patch가 나오면,
  C20 scope에서만 Stage2 bridge/guard를 적용하고,
  C20 점수비중은 수출/채널/반복수요/OPM/EPS revision 중심으로 재합산한다.
```

## Promotion Decision

모든 후보 축은 네 가지 중 하나로 분류한다.

| decision | 의미 |
|---|---|
| `apply_next_patch` | 지금 작은 패치로 적용 가능 |
| `hold_for_more_evidence` | 근거 수나 전이 경로가 부족 |
| `blocked_by_data_quality` | evidence URL, source proxy, 가격경로 등 품질 문제 |
| `blocked_by_logic_risk` | E2R 철학상 위험, Green 제한 필요 |

중요한 원칙:

```text
apply_next_patch가 있으면 다음 연구만 더 요구하지 말고 실제 profile에 반영한다.
hold/block이면 왜 막혔는지 보고서에 명확히 남긴다.
```

## Safe Patch Axis

현재 active profile에 들어갈 수 있는 v12 safe patch와 runtime weight는 다음 종류다.

| axis | 의미 |
|---|---|
| `stage2_bonus_candidate_delta` | 비가격 증거가 있을 때 해당 scope Stage2 근처에 최대 +1 |
| `stage2_required_bridge` | 해당 scope Stage2에 비가격 bridge 요구 |
| `local_4b_watch_guard` | 가격만 오른 4B는 watch로 제한 |
| `full_4b_overlay_candidate` | full 4B는 비가격 증거 필요 |
| `earlier_thesis_break_watch` | thesis-break watch를 더 일찍 표시 |
| `hard_4c_confirmation` | 비가격 thesis-break 확인 시 4C 강화 |
| `archetype_weight_runtime` | canonical archetype별 score component 비중을 다르게 적용 |

Stage 3-Green은 쉽게 만들지 않는다.

```text
v12는 Green 완화가 아니라
Stage2/Yellow 관찰 개선,
4B/4C 보호,
price-only false positive 차단을 우선한다.
```

## 아키타입별 점수비중 반영

`run-v12-calibration`은 이제 다음 파일도 생성한다.

```text
configs/e2r_archetype_weight_profile_v2_2.json
reports/e2r_calibration/v12/archetype_weight_runtime_report.md
```

예시:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  EPS/FCF 22
  visibility 23
  bottleneck/pricing 12
  mispricing 16
  valuation 13
  capital 4
  information 10

의미:
  삼양식품/실리콘투 계열은 계약공시가 없어도
  수출 증가, 채널 확장, 반복수요, OPM, EPS revision이 강하면 점수 기여가 커진다.
```

반대로:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  visibility 24
  bottleneck/pricing 17

의미:
  전력기기/방산 계열은 계약금액, 수주잔고, 정부 고객, 납품 visibility가 약하면
  가격이 먼저 올라도 Stage 3 쪽으로 쉽게 못 간다.
```

과거 가격경로는 다음 용도다.

```text
사용 가능:
  과거 Stage2 이후 MFE/MAE, peak, 4B/4C 타이밍을 보고 weight profile을 보정한다.

사용 금지:
  as_of_date 당일 점수 계산에 미래 MFE/peak를 직접 넣는다.
```

## 런타임 연결 조건

v12 scoped patch가 실제 점수에 작동하려면 `ScoringPayload`에 다음 중 하나가 있어야 한다.

```text
large_sector_id
canonical_archetype_id
```

예시:

```text
payload:
  canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
  evidence_family_financial_actual = 1
  evidence_family_disclosure = 1
  eps_fcf_explosion >= Stage2 기준

결과:
  C22 Stage2 bonus scope가 active profile에 있으면 최대 +1이 붙을 수 있다.
```

반대로:

```text
payload:
  canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
  price_only_blowoff_score = 80
  비가격 증거 없음

결과:
  보너스 없음.
  positive Stage 승격도 price-only guard에 막힌다.
```

fallback은 정상 성공으로 숨기지 않는다.

```text
payload:
  canonical_archetype_id 없음
  large_sector_id 없음

결과:
  archetype_weight_fallback_used = 1
  archetype_weight_fallback_missing_scope = 1

의미:
  이 후보는 아키타입별 점수비중이 적용되지 않았다.
  mapper 또는 feature pipeline의 sector/archetype 연결을 고쳐야 한다.
```

또 다른 예시:

```text
payload:
  canonical_archetype_id = UNKNOWN_ARCHETYPE
  large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION

결과:
  large sector weight는 적용될 수 있지만
  archetype_weight_canonical_missing_large_sector_fallback = 1

의미:
  완전한 C20/C18/C19 같은 canonical archetype 매핑은 실패했고,
  임시로 L5 대섹터 weight만 쓴 것이다.
```

## 필수 산출물

데이터:

```text
data/e2r/calibration/v12/v12_md_registry.jsonl
data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl
data/e2r/calibration/v12/rejected_v12_rows.jsonl
data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl
data/e2r/calibration/v12/v12_aggregate_metrics.json
data/e2r/calibration/v12/stage_transition_summary.jsonl
data/e2r/calibration/v12/v12_promotion_decisions.jsonl
data/e2r/calibration/v12/v12_patch_specs.jsonl
configs/e2r_scoring_profile_v2_2.yaml
configs/e2r_archetype_weight_profile_v2_2.json
configs/e2r_scoring_profile_active.yaml
```

보고서:

```text
reports/e2r_calibration/v12/ingest_summary.md
reports/e2r_calibration/v12/apply_next_patch_plan.md
reports/e2r_calibration/v12/blocked_axes_report.md
reports/e2r_calibration/v12/rolling_calibration_apply_report.md
reports/e2r_calibration/v12/rolling_calibration_apply_summary.json
reports/e2r_calibration/v12/archetype_weight_runtime_report.md
```

## 금지 사항

```text
종목명 하드코딩 금지
benchmark label을 scoring input으로 사용 금지
case library를 후보 생성 input으로 사용 금지
Stage 3-Green 전역 기준 완화 금지
미래 데이터 사용 금지
가격만 오른 row를 Green 또는 full 4B로 승격 금지
투자 권고 문구 금지
자동매매 또는 증권사 API 연결 금지
```

## 확인해야 할 핵심 결과

최근 v12 배치 기준 정상 예시는 다음과 같다.

```text
v12_result_md_count: 87
v12_validated_trigger_rows: 960
v12_representative_trigger_rows: 748
stage_transition_summary_rows: 410
large_sectors_covered: 10
canonical_archetypes_covered: 27
applied_patch_count: 64
archetype_weight_count: 27
large_sector_weight_count: 10
production_default_scoring_changed: true
active_profile: e2r_2_2
rollback_profile: calibrated
```

숫자는 새 배치가 들어오면 달라질 수 있다. 중요한 것은 다음이다.

```text
1. v12 MD가 0개면 실패한다.
2. trigger row가 0개면 실패한다.
3. rejected row는 이유를 남긴다.
4. apply_next_patch는 active v2.2 profile에 반영된다.
5. hold/block은 다음 연구 또는 데이터 보강 대상으로 남긴다.
```

## 검증 명령

문서만 고쳤을 때 최소:

```bash
git diff --check
```

파이프라인이나 profile 로직을 고쳤을 때:

```bash
PYTHONPATH=src python -m unittest tests.test_calibration_v12_pipeline -v
PYTHONPATH=src python -m unittest tests.test_calibration_pipeline -v
PYTHONPATH=src python -m compileall -q src tests
git diff --check
```

점수, Stage, calibration 로직을 건드렸을 때:

```bash
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 완료 기준

```text
docs/core/Architecture.md가 최신 흐름을 설명한다.
docs/core/goal.md가 run-v12-calibration 중심으로 정리되어 있다.
run-v12-calibration이 기본 적용 플로우로 명시되어 있다.
run-v12-full은 진단 플로우로만 설명되어 있다.
active profile은 e2r_2_2, rollback은 calibrated로 설명되어 있다.
archetype weight runtime profile이 점수비중 반영 흐름으로 명시되어 있다.
Stage 3-Green 완화 금지와 price-only guard가 명시되어 있다.
```
