# Semis Green Recall Score Audit - 2026-06-19

## 결론

사용자 문제제기가 맞다. SK하이닉스 같은 HBM 구조적 winner가 2023~2024 구간에서 전혀 Green 또는 강한 Stage로 잡히지 않았다면 시스템 문제다.

다만 지금 확인한 문제는 두 층이다.

1. 연구자료는 이미 SK하이닉스를 과거 HBM 구조적 성공 케이스로 기록했다.
2. 운영 파이프라인은 그 연구축을 현재 실행 feature/score로 완전히 번역하지 못하고 있다.

쉬운 예:

- 연구자료: "2024-04-25 SK하이닉스는 HBM sold-out capacity + Q1 실적 surprise + revision bridge가 있어 Green."
- 운영 scorer: "현재 입력에는 revision source, FCF source, OP source, 독립 consensus revision이 안 보인다. 그래서 Green은 못 준다."

이 둘은 다른 말이다. 연구 판단은 맞게 쌓였는데, 운영 점수화 경로가 아직 덜 따라온 것이다.

## 현재 Green 기준

활성 profile은 `configs/e2r_scoring_profile_v2_2.yaml`이다.

| Gate | 기준 |
| --- | ---: |
| Stage2 total | 65 |
| Stage3-Yellow total | 75 |
| Stage3-Green total | 87 |
| Green EPS/FCF | 17 |
| Green visibility | 15 |
| Green bottleneck | 15 |
| Green mispricing | 10 |
| Green valuation | 10 |
| Green revision | 55 |
| Green structural visibility | 45 |

중요한 guardrail:

- `archetype_weight_runtime_enabled: true`
- `stage3_green_not_loosened_by_v12: true`

즉 연구 누적으로 아키타입별 점수 비중은 바뀌지만, Green 문턱 자체는 낮아지지 않는다.

## 2026-06-12 현재 실행 점수

대상 실행:

- 삼성전자: `output/0618_green_gate_live_patched_2026-06-12/005930/korea_live_lite/2026-06-12_run_log.json`
- SK하이닉스: `output/0618_green_gate_live_patched_2026-06-12/000660/korea_live_lite/2026-06-12_run_log.json`

### 삼성전자 005930

| 항목 | raw | C06 가중 후 |
| --- | ---: | ---: |
| EPS/FCF | 20.0000 | 24.0000 |
| 실적가시성 | 13.9341 | 14.6308 |
| 병목/가격 | 16.2009 | 15.3909 |
| 미스프라이싱 | 11.0405 | 11.0405 |
| 밸류에이션 | 9.9790 | 7.9832 |
| 자본정책 | 2.0183 | 1.6146 |
| 정보신뢰 | 3.7500 | 3.7500 |
| 합계 | 76.9228 | 78.4100 |

Stage: `3-Yellow`  
Green total gap: `87 - 78.41 = 8.59`

Green gate별 통과/실패:

| Gate | 현재 | 기준 | 차이 | 결과 |
| --- | ---: | ---: | ---: | --- |
| total | 78.4100 | 87 | -8.5900 | 실패 |
| EPS/FCF | 20.0000 | 17 | +3.0000 | 통과 |
| visibility | 13.9341 | 15 | -1.0659 | 실패 |
| bottleneck | 16.2009 | 15 | +1.2009 | 통과 |
| mispricing | 11.0405 | 10 | +1.0405 | 통과 |
| valuation | 9.9790 | 10 | -0.0210 | 실패 |

삼성전자가 Green이 아닌 직접 이유:

- 총점이 Green 87보다 8.59점 낮다.
- 실적가시성이 raw 13.9341로 Green 기준 15 미달이다.
- 밸류에이션이 raw 9.979로 Green 기준 10에 아주 근소하게 미달이다.
- FCF source가 없다.
- revision은 잡혔지만 report-derived proxy라 강한 독립 consensus revision으로 보기 어렵다.
- score-gap 확장이 provider timeout으로 끝났다.

쉬운 예:

- 엔진은 좋다: EPS/FCF 20점 만점.
- 길도 어느 정도 좋다: 병목/미스프라이싱은 통과.
- 그런데 연료계와 계기판이 부족하다: FCF, durable revision, 독립 consensus revision이 약하다.

### SK하이닉스 000660

| 항목 | raw | C06 가중 후 |
| --- | ---: | ---: |
| EPS/FCF | 20.0000 | 24.0000 |
| 실적가시성 | 13.5256 | 14.2019 |
| 병목/가격 | 14.9822 | 14.2331 |
| 미스프라이싱 | 6.0620 | 6.0620 |
| 밸류에이션 | 8.6446 | 6.9157 |
| 자본정책 | 2.1220 | 1.6976 |
| 정보신뢰 | 3.7500 | 3.7500 |
| 합계 | 69.0864 | 70.8603 |

Stage: `2`  
Yellow total gap: `75 - 70.8603 = 4.1397`  
Green total gap: `87 - 70.8603 = 16.1397`

Green gate별 통과/실패:

| Gate | 현재 | 기준 | 차이 | 결과 |
| --- | ---: | ---: | ---: | --- |
| total | 70.8603 | 87 | -16.1397 | 실패 |
| EPS/FCF | 20.0000 | 17 | +3.0000 | 통과 |
| visibility | 13.5256 | 15 | -1.4744 | 실패 |
| bottleneck | 14.9822 | 15 | -0.0178 | 실패 |
| mispricing | 6.0620 | 10 | -3.9380 | 실패 |
| valuation | 8.6446 | 10 | -1.3554 | 실패 |

하이닉스가 이번 실행에서 낮아진 직접 이유:

- consensus `0`
- consensus revisions `0`
- selected OP source `null`
- selected FCF source `null`
- selected revision source `null`
- price/theme momentum은 강한데 revision source가 없어서 theme-overheat guard가 작동한다.

쉬운 예:

- 이미 많이 오른 종목인데 "왜 더 싸고 더 좋아졌는지"를 숫자로 못 읽으면, scorer는 "좋은 회사"가 아니라 "오른 테마"로 본다.
- 하이닉스 자체가 나쁘다는 뜻이 아니라, 현재 실행 입력이 HBM 매출/마진/revision/FCF를 구조화하지 못했다는 뜻이다.

## 예전 실행과 현재 실행이 다른 이유

2026-06-11 deep recheck에서는 점수가 더 높았다.

| 종목 | Stage | 총점 | 핵심 출처 | Green 미달 이유 |
| --- | --- | ---: | --- | --- |
| 삼성전자 | 3-Yellow | 80.1102 | CompanyGuide snapshot | 총점 87 미달, visibility/bottleneck 미달, backlog/RPO/FCF/CAPEX bridge 부족 |
| SK하이닉스 | 3-Yellow | 83.0245 | CompanyGuide snapshot + report_proxy OP | 총점 87 미달, revision/FCF 출처 부재, backlog/RPO/FCF/direct AI revenue bridge 부족 |

따라서 SK하이닉스가 항상 70점대였던 것은 아니다. 최신 `0618 patched` 실행은 입력 변환 상태가 더 나빠졌다.

특히 하이닉스는 deep run에서:

- 실적가시성 14.0403
- 병목/가격 16.7702
- 미스프라이싱 11.9811
- 밸류에이션 11.7118
- 총점 83.0245

까지 갔다. 그래도 Green은 아니었는데, 그때의 미달 이유는 revision/FCF source 부재와 Green 총점 87 미달이었다.

## 연구자료의 과거 정답표

연구자료는 SK하이닉스를 놓친 것이 아니라, 명확히 성공 케이스로 기록했다.

| 종목 | 날짜 | 연구 Stage | 핵심 evidence | MFE90 | MAE90 | verdict |
| --- | --- | --- | --- | ---: | ---: | --- |
| SK하이닉스 | 2023-10-27 | Stage2-Actionable | Q3 HBM/AI-memory traction | 46.85 | -2.35 | current_profile_missed_structural |
| SK하이닉스 | 2024-02-22 | Stage2-Actionable | HBM customer capacity bridge | 58.79 | -2.04 | source_proxy blocks production delta |
| SK하이닉스 | 2024-04-26 | Stage3-Green | Q1 surprise + HBM sold/booked-out capacity | 39.76 | -14.74 | current_profile_correct |
| SK하이닉스 | 2024-07-11 | Stage4B-Overlay | local price peak after HBM rally | 3.11 | -39.96 | price-only local 4B too early |

즉 "하닉은 예전에 잡았어야 한다"는 연구자료 기준으로 맞다. 다음 검증은 운영 파이프라인을 `as_of_date=2024-04-25` 또는 `2024-04-26`으로 replay해서 실제로 Green이 나오는지 확인해야 한다.

삼성전자는 연구자료상 같은 C06이라도 결론이 다르다.

| 종목 | 날짜 | 연구 Stage | 핵심 evidence | MFE90 | MAE90 | verdict |
| --- | --- | --- | --- | ---: | ---: | --- |
| 삼성전자 | 2024-01-03 | Stage2-Watch | generic memory/HBM optimism, direct qualification 없음 | 11.69 | -8.18 | false positive 방지 |
| 삼성전자 | 2024-03-20 | Stage3-Yellow/Weak-Green | HBM catch-up 기대, named qualification 없음 | 15.21 | -4.42 | false Green |
| 삼성전자 | 2024-05-24 | Stage4C thesis-break watch | HBM Nvidia qualification issue | 16.73 | -21.08 | 4C too late |
| 삼성전자 | 2024-08-07 | Stage4B | HBM3E headline but margin/revision bridge 없음 | 4.69 | -29.05 | false positive |

삼성전자는 "HBM 대장 winner"로 일찍 Green을 줘야 했던 케이스라기보다, 연구자료상 "HBM catch-up headline만으로 Green 주면 위험"한 케이스로 더 많이 기록되어 있다. 이후 2025~2026 다른 창에서는 별도 replay가 필요하다.

## 코드상 점수가 깎이는 위치

### 1. Green gate가 빡세다

`src/e2r/staging.py`는 total, EPS/FCF, visibility, bottleneck, mispricing, valuation, revision, structural visibility를 모두 요구한다. 하나만 좋아도 Green이 아니다.

예:

- EPS/FCF 20점 만점이어도 revision_score가 55 미만이면 Green 실패.
- bottleneck이 좋아도 FCF/revision/visibility가 비면 Green 실패.

### 2. C06 weight는 적용되지만, Green gate는 느슨해지지 않는다

`src/e2r/calibration/archetype_weight_profile.py`는 raw component를 아키타입별 weight max로 재계산한다.

C06 weight:

| component | C06 max |
| --- | ---: |
| EPS/FCF | 24 |
| visibility | 21 |
| bottleneck | 19 |
| mispricing | 15 |
| valuation | 12 |
| capital | 4 |
| information | 5 |

그래서 삼성/하닉 모두 EPS/FCF는 20 raw가 24 weighted로 올라간다. 하지만 Green gate는 여전히 total 87, revision 55, structural visibility 45를 요구한다.

### 3. CompanyGuide의 "EPS 상향"이 revision score로 충분히 안 들어간다

`src/e2r/sources/company_guide.py`는 recent report에서 다음 field를 만든다.

- `target_price_upgrade_mentioned`
- `eps_revision_up_mentioned`

그런데 `src/e2r/features.py`의 `_revision_score()`는 다음만 본다.

- numeric `eps_revision_pct`
- numeric `op_revision_pct`
- numeric `fcf_revision_pct`
- numeric `target_price_revision_pct`
- `estimate_upgrade_mentioned`
- `target_price_upgrade_mentioned`
- `earnings_beat_mentioned`

문제:

- `eps_revision_up_mentioned`는 만들어지지만 `_revision_score()`에서 직접 쓰지 않는다.
- 그래서 리포트가 "추정 EPS 상향"이라고 해도 numeric revision이 없으면 Green revision 55를 못 채우기 쉽다.

쉬운 예:

- 사람이 보면 "EPS 상향 리포트가 여러 개네"라고 판단한다.
- 현재 scorer는 "상향률 몇 %인지, 또는 estimate_upgrade_mentioned인지"가 없으면 revision 점수를 크게 못 준다.

### 4. report proxy revision은 숫자가 있어야 만들어진다

`src/e2r/research/report_consensus_proxy.py`는 report에서 `ConsensusRevision`을 만들 때 numeric revision 값을 요구한다.

즉 다음은 revision source가 된다.

- EPS 1개월 상향률 +12%
- OP revision +20%
- target price revision +15%

하지만 다음은 현재 약하다.

- "추정 EPS 상향"
- "목표주가 상향"
- "HBM 믹스 개선으로 실적 추정치 상향"

방향성 문장은 field로 잡히지만, consensus revision family로는 약하게 들어간다.

### 5. 독립 consensus/revision family가 보수적으로 계산된다

`src/e2r/features.py`의 evidence family diagnostics는 independent consensus와 independent revision만 Green family로 강하게 본다. report-derived proxy는 별도 proxy family로 표시된다.

그래서 리포트가 많아도:

- independent consensus `0`
- independent consensus_revision `0`

이면 Green gate에서 불리하다.

### 6. 연구축이 운영 feature로 완전히 번역되지 않았다

연구자료의 C06 shadow score는 이런 축을 쓴다.

- `hbm_customer_qualification_score`
- `customer_allocation_visibility_score`
- `capacity_or_shipment_score`
- `margin_bridge_score`
- `revision_score`
- `customer_quality_score`

운영 scorer의 HBM domain score는 주로 이런 boolean key를 본다.

- `hbm_demand_mentioned`
- `memory_price_increase_mentioned`
- `supply_discipline_mentioned`
- `customer_preorder_or_allocation`
- `minimum_revenue_guarantee`
- `hbm_capacity_constraint`
- `advanced_packaging_bottleneck`

두 목록이 완전히 같지 않다. 그래서 연구자료에서 중요하다고 한 `sold-out capacity`, `qualified customer allocation`, `HBM mix margin bridge`가 운영 점수에서는 일부만 반영될 수 있다.

## 전체 아키타입도 같은 위험이 있다

V12 aggregate metric 기준:

| scope | rows | positive | counter | profile errors | false positive | missed structural | too late | source proxy only | URL pending |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| global | 12,471 | 1,495 | 2,628 | 6,257 | 3,559 | 317 | 1,680 | 3,723 | 3,906 |
| L2 AI/Semi | 1,384 | 246 | 349 | 805 | 436 | 52 | 216 | 319 | 414 |
| C06 HBM | 229 | 32 | 56 | 150 | 66 | 11 | 36 | 63 | 78 |

해석:

- 이 문제는 HBM만의 문제가 아니다.
- 많은 연구자료가 "현재 profile이 아직 틀린다"고 표시한다.
- weight profile은 반영됐지만, 세부 연구축을 운영 parser/feature/gate에 연결하는 작업이 아직 남아 있다.

## 최종 판단

현재 시스템이 하는 판단은 이렇다.

1. EPS/FCF 폭발은 강하게 준다.
2. HBM 병목도 일부 준다.
3. 하지만 Green은 "진짜 돈으로 잠긴 증거"를 요구한다.
4. 그 증거는 OP/FCF/revision/고객 allocation/장기 capacity/order/margin bridge로 들어와야 한다.
5. 현재 parser는 이 증거를 연구자료만큼 잘 구조화하지 못한다.

따라서 지금 고쳐야 할 것은 "하닉을 하드코딩해서 Green"이 아니다.

다음 패치 방향:

1. SK하이닉스 C06 historical replay를 만든다.
   - `as_of_date=2023-10-27`
   - `as_of_date=2024-02-22`
   - `as_of_date=2024-04-25/26`
   - `as_of_date=2024-07-11`
2. 삼성전자 C06 false-positive replay를 만든다.
   - `2024-03-20`
   - `2024-05-24`
   - `2024-08-07`
3. CompanyGuide `eps_revision_up_mentioned`를 revision score에 연결한다.
4. report directional revision을 source-backed proxy revision으로 승격할 조건을 만든다.
5. C06 연구축을 운영 parsed fields에 매핑한다.
   - sold/booked-out capacity
   - qualified customer allocation
   - HBM mix margin bridge
   - capacity/customer lock
6. 같은 방식으로 C11/C20/C21/C22/C28 등 Green 사례도 replay해 cross-archetype 변환 누락을 찾는다.

투자 권고가 아니라 파이프라인 진단 기록이다.
