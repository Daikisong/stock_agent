# HBM As-Of Replay Autopsy - 2026-06-19

## 결론

사용자 문제제기가 맞다. SK하이닉스 같은 HBM 구조적 winner가 과거 replay에서 Green으로 올라오지 못하면, "자료 부족"이라고만 설명하면 안 된다.

이번 점검에서 확인된 핵심은 다음이다.

- SK하이닉스 2024-04-30 replay는 Stage 3-Yellow까지는 올라왔다.
- 그런데 Green은 `failed_stage3_total_score`, `failed_stage3_bottleneck`에서 막혔다.
- EPS/FCF, revision, visibility, valuation은 대부분 통과권이다.
- 실제 문제는 HBM 구조 증거가 최종 `bottleneck_pricing` component로 충분히 번역되지 않는 것이다.
- 삼성전자 2024-04-30은 점수에서 떨어진 것이 아니라 `failed_official_cheap_scan`으로 후보 진입 전 단계에서 빠졌다.

쉬운 예:

- 연구자료: "HBM 수요, 고객 allocation, sold/booked-out capacity, Q1 surprise가 있으니 Green."
- 현재 replay scorer: "HBM 관련 문장은 읽었지만, 최종 병목 점수는 11.63/20이라 Green 병목 기준 15/20에는 못 미친다."

## 실행한 Replay

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2024-04-01 \
  --end-date 2024-04-01 \
  --frequency daily \
  --output-directory output/0619_asof_replay_hbm_2024_04_01 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --no-theme-rebalance
```

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2024-04-30 \
  --end-date 2024-04-30 \
  --frequency daily \
  --output-directory output/0619_asof_replay_hbm_2024_04_30 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --no-theme-rebalance
```

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2024-04-25 \
  --end-date 2024-04-25 \
  --frequency daily \
  --output-directory output/0619_asof_replay_hbm_2024_04_25 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --no-theme-rebalance
```

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2024-04-26 \
  --end-date 2024-04-26 \
  --frequency daily \
  --output-directory output/0619_asof_replay_hbm_2024_04_26 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --no-theme-rebalance
```

```bash
PYTHONPATH=src python -m e2r.cli.analyze_asof_stage_promotion \
  --asof-output output/0619_asof_replay_hbm_2024_04_30/2024-04-30_to_2024-04-30 \
  --output-directory output/0619_asof_stage_promotion_hbm_2024_04_30 \
  --top-candidates 10 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10
```

## 2024-04-01 Replay 결과

| symbol | name | stage | score | 핵심 미달 |
| --- | --- | --- | ---: | --- |
| 000660 | SK하이닉스 | 3-Yellow | 76.0596 | Green total/bottleneck 미달 |
| 005930 | 삼성전자 | 2 | 68.6752 | Green total/visibility/bottleneck 등 미달 |

SK하이닉스 2024-04-01 score components:

| component | score |
| --- | ---: |
| EPS/FCF | 20.0000 |
| visibility | 14.7057 |
| bottleneck | 11.3960 |
| mispricing | 12.8520 |
| valuation | 12.3390 |
| capital | 0.0865 |
| confidence | 3.0000 |
| total | 76.0596 |

삼성전자 2024-04-01 score components:

| component | score |
| --- | ---: |
| EPS/FCF | 20.0000 |
| visibility | 12.4403 |
| bottleneck | 9.9143 |
| mispricing | 11.5980 |
| valuation | 11.6985 |
| capital | 0.0615 |
| confidence | 3.0000 |
| total | 68.6752 |

## 2024-04-25/26 Green 정답일 Replay 결과

연구 장부에서 SK하이닉스는 2024-04-25/26 `Stage3-Green` 정답 사례다. 그런데 runtime replay는 두 날짜 모두 Green을 하나도 만들지 못했다.

| date | symbol | name | stage | score | failed gates |
| --- | --- | --- | --- | ---: | --- |
| 2024-04-25 | 000660 | SK하이닉스 | 3-Yellow | 76.0596 | `failed_stage3_total_score`, `failed_stage3_visibility`, `failed_stage3_bottleneck` |
| 2024-04-26 | 000660 | SK하이닉스 | 3-Yellow | 76.0596 | `failed_stage3_total_score`, `failed_stage3_visibility`, `failed_stage3_bottleneck` |

두 날짜의 SK하이닉스 component는 같다.

| component | score |
| --- | ---: |
| EPS/FCF | 20.0000 |
| visibility | 14.7057 |
| bottleneck | 11.3960 |
| mispricing | 12.8520 |
| valuation | 12.3390 |
| capital | 0.0865 |
| confidence | 3.0000 |
| total | 76.0596 |

진단값:

| diagnostic | value |
| --- | ---: |
| revision_score | 100.0000 |
| domain_specific_evidence_score | 80.0000 |
| medium_term_revision_visibility | 100.0000 |
| structural_visibility_quality | 70.7335 |
| sector_visibility_score | 70.4725 |
| sector_bottleneck_score | 51.1150 |
| contract_quality | 0.0000 |
| backlog_rpo_visibility | 15.0000 |
| capa_constraint | 0.0000 |
| asp_pricing_power | 20.0000 |
| fcf_quality_score | 0.0000 |

입력 coverage:

| input | count |
| --- | ---: |
| price_bars | 2 |
| financial_actuals | 1 |
| disclosures | 1 |
| research_reports | 1 |
| news_items | 0 |
| consensus | 2 |
| consensus_revisions | 1 |

해석:

- 2024-04-25/26에는 후보 진입과 web research까지 됐다.
- `revision_score`, `domain_specific_evidence_score`, `structural_visibility_quality`는 충분히 높다.
- 그래도 Green gate는 `visibility 14.7057 < 15`, `bottleneck 11.396 < 15`, `total 76.0596 < 87`에서 막힌다.
- 즉 연구 정답일에도 `HBM sold/booked-out capacity`가 `capa_constraint`, `backlog_rpo_visibility`, `contract_quality`, `fcf_quality`로 충분히 변환되지 않았다.

쉬운 예:

- 연구자료는 "HBM 물량이 잠겼고 Q1 surprise까지 확인됐다"고 썼다.
- runtime은 "HBM 관련성은 80점, revision은 100점. 그런데 CAPA 잠김 0점, 계약품질 0점, FCF 품질 0점"으로 봤다.

## 2024-04-30 Replay 결과

| symbol | name | stage | score | 핵심 미달 |
| --- | --- | --- | ---: | --- |
| 000660 | SK하이닉스 | 3-Yellow | 76.7639 | `failed_stage3_total_score`, `failed_stage3_bottleneck` |
| 005930 | 삼성전자 | not analyzed | n/a | `failed_official_cheap_scan` |

삼성전자는 2024-04-30 stage gate에서 떨어진 것이 아니라 cheap scan 후보 단계에서 빠졌다. 따라서 이 결과만으로 "삼성전자가 점수는 충분했는데 Green gate에서 막혔다"고 보면 안 된다.

## SK하이닉스 2024-04-30 상세 점수

Green gate 기준:

| gate | 기준 | SK하이닉스 | 결과 |
| --- | ---: | ---: | --- |
| total | 87.0000 | 76.7639 | 실패 |
| EPS/FCF | 17.0000 | 20.0000 | 통과 |
| visibility | 15.0000 | 15.1502 | 통과 |
| bottleneck | 15.0000 | 11.6339 | 실패 |
| mispricing | 10.0000 | 12.8520 | 통과 |
| valuation | 10.0000 | 12.3390 | 통과 |
| revision | 55.0000 | 100.0000 | 통과 |
| structural visibility | 45.0000 | 71.3652 | 통과 |

아키타입 weight 적용 후 실제 total에 들어간 값:

| component | raw score | C06 max | weighted score | Green effective threshold | 결과 |
| --- | ---: | ---: | ---: | ---: | --- |
| EPS/FCF explosion | 20.0000 / 20 | 24 | 24.0000 | 20.4000 | 통과 |
| earnings visibility | 15.1502 / 20 | 21 | 15.9077 | 15.7500 | 통과 |
| bottleneck pricing | 11.6339 / 20 | 19 | 11.0522 | 14.2500 | 실패 |
| market mispricing | 12.8520 / 15 | 15 | 12.8520 | 10.0000 | 통과 |
| valuation rerating | 12.3390 / 15 | 12 | 9.8712 | 8.0000 | 통과 |
| capital allocation | 0.1010 / 5 | 4 | 0.0808 | n/a | n/a |
| information confidence | 3.0000 / 5 | 5 | 3.0000 | n/a | n/a |

즉 C06 weight가 하닉을 깎은 것이 아니다. C06 weight 적용 전 raw 합은 약 `75.0761`이고, 적용 후 total은 `76.7639`로 오히려 약 `+1.6878` 올라간다. 그래도 Green total `87`까지는 `10.2361`점 모자란다.

더 중요한 점:

- bottleneck만 Green threshold까지 올려도 total은 약 `79.9617`에 그친다.
- 따라서 병목 변환만 고치면 끝이 아니고, capacity/customer/FCF/confidence가 total로 더 들어와야 한다.
- 예: `HBM sold-out`을 `hbm_capacity_pre_sold`, `capacity_precommitted`, `customer_preorder_or_allocation`, `opm_expansion_pctp`, `actual_fcf` 같은 필드로 쪼개서 넣어야 한다.

점수 component:

| component | score | 만점 |
| --- | ---: | ---: |
| EPS/FCF explosion | 20.0000 | 20 |
| earnings visibility | 15.1502 | 20 |
| bottleneck pricing | 11.6339 | 20 |
| market mispricing | 12.8520 | 15 |
| valuation rerating | 12.3390 | 15 |
| capital allocation | 0.1010 | 5 |
| information confidence | 3.0000 | 5 |
| total | 76.7639 | 100 |

진단 sub-score:

| diagnostic | value |
| --- | ---: |
| revision_score | 100.0000 |
| price_stage_score | 9.7436 |
| contract_quality | 0.0000 |
| backlog_rpo_visibility | 15.0000 |
| capa_constraint | 0.0000 |
| asp_pricing_power | 20.0000 |
| structural_shortage | 68.4000 |
| one_off_shortage_risk | 0.0000 |
| structural_visibility_quality | 71.3652 |
| sector_visibility_score | 71.2060 |
| sector_bottleneck_score | 51.6040 |
| medium_term_revision_visibility | 100.0000 |
| domain_specific_evidence_score | 80.0000 |

읽은 evidence family:

| present | missing |
| --- | --- |
| price, financial_actual, disclosure, research_report | consensus, consensus_revision, news |

중요한 모순:

- 입력 count에는 report-derived consensus/revision proxy가 있다.
- 그러나 Green family 진단에서는 independent consensus/revision/news가 missing으로 남는다.
- 그래서 보고서 기반 추정치는 점수에는 일부 들어가지만, Green 확신도를 높이는 독립 evidence family로는 약하게 취급된다.

## 왜 Bottleneck이 낮게 환산되는가

`src/e2r/features.py`의 최종 component 계산은 다음 구조다.

```python
sector_bottleneck_raw = (
    sector_metrics["sector_bottleneck_score"] * 0.60
    + sub_scores.asp_pricing_power * 0.25
    + sub_scores.structural_shortage * 0.15
)

bottleneck_pricing = bottleneck_raw / 100.0 * 20.0
```

actual conversion bridge가 있으면 아래 대체식도 비교한다.

```python
bottleneck_raw = max(
    bottleneck_raw,
    actual_conversion * 0.25
    + sector_metrics["sector_bottleneck_score"] * 0.35
    + sub_scores.structural_shortage * 0.25
    + sub_scores.asp_pricing_power * 0.15,
)
```

즉 `domain_specific_evidence_score=80`이어도 곧바로 `bottleneck_pricing=16/20`이 되는 것이 아니다. 먼저 sector bottleneck, ASP, structural shortage, actual conversion으로 다시 섞이고, 마지막에 20점 만점으로 압축된다.

쉬운 예:

- 연구자료 점수: "HBM 증거 80점."
- 운영 점수: "그 80점을 병목 component에 100% 넣지 않고, 여러 축 중 일부로만 반영한 뒤 20점 만점으로 환산."
- 결과: HBM 증거는 강한데 최종 Green 병목 점수는 11.63점.

## 무엇이 잘못됐나

이번 replay 기준으로 하닉이 Green이 아닌 이유는 "하닉 thesis가 약해서"가 아니다.

문제는 더 구체적이다.

1. C06 연구축이 최종 component에 과소 변환된다.
   - `domain_specific_evidence_score=80`
   - `medium_term_revision_visibility=100`
   - `structural_visibility_quality=71.3652`
   - 그런데 최종 `bottleneck_pricing=11.6339`

2. HBM capacity/customer evidence가 generic `contract_quality`, `backlog_rpo_visibility`, `capa_constraint`로 충분히 들어가지 못한다.
   - `contract_quality=0`
   - `capa_constraint=0`
   - `backlog_rpo_visibility=15`

3. 독립 consensus/revision/news family가 비어 Green 확신이 약하게 보인다.
   - report proxy는 존재하지만 independent family로는 missing.

4. 삼성전자는 stage 점수 문제가 아니라 후보 진입 문제도 있다.
   - 2024-04-30 삼성전자는 `failed_official_cheap_scan`.

## 다음 패치 후보

1. C06 HBM conversion patch
   - `sold/booked-out capacity`, `customer allocation`, `advanced packaging bottleneck`, `HBM capacity constraint`를 `capa_constraint`, `customer_preorder_or_allocation`, `backlog/visibility`에 더 직접 연결한다.

2. C06 bottleneck component patch
   - source-backed HBM demand + allocation + capacity constraint + ASP + revision이 동시에 있으면 final `bottleneck_pricing`이 Green threshold 근처까지 올라가도록 변환식을 점검한다.

3. Report proxy confidence patch
   - report-derived consensus/revision을 무조건 독립 family로 승격하면 false positive가 생길 수 있다.
   - 대신 source-backed broker report가 여러 개이고 날짜가 as-of 이전이며 숫자 추정치가 있으면 Green family confidence를 부분 인정하는 방식이 필요하다.

4. Historical replay fixture 확장
   - SK하이닉스 연구 정답일인 2024-04-26 Q1 surprise + sold/booked-out capacity fixture를 직접 넣어야 한다.
   - 현재 local fixture는 2024-04-01 broker report 중심이라 연구자료의 2024-04-26 Green trigger와 완전히 같지 않다.

## 현재 판단

현재 replay는 과거 하닉을 완전히 놓친 것은 아니다. 2024-04-30 기준 Stage 3-Yellow 76.7639까지는 잡았다.

하지만 사용자가 기대한 "구조적 HBM winner면 Green으로 잡았어야 한다"는 기준에서는 실패다. 실패 원인은 단순 자료 부족이 아니라, 연구자료의 HBM 세부축이 운영 점수의 `bottleneck_pricing`, `contract_quality`, `capa_constraint`, `backlog_visibility`, 독립 evidence family로 충분히 변환되지 않는 것이다.
