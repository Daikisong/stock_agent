# Global Green Runtime Gap Autopsy - 2026-06-19

## 결론

삼성전자/SK하이닉스만 이상한 것이 아니다. 현재 문제는 전역 구조 문제다.

누적 연구자료는 실제로 Green 사례와 반례를 많이 쌓았다. 하지만 운영 scorer에 반영된 것은 주로 다음 두 가지다.

1. canonical archetype별 7개 큰 component 배점
2. 일부 rolling guardrail scope

반대로 연구자료의 세부 점수축은 아직 운영 feature로 직접 번역되지 않는다.

쉬운 예:

- 연구자료: `margin_bridge_score=9`, `customer_quality_score=8`, `revision_score=8`이라 Green.
- 운영 scorer: `op_revision_pct`, `fy1_op`, `actual_op_yoy_pct`, `customer_preorder_or_allocation`, `order_backlog_to_sales` 같은 normalized field가 있어야 점수가 오른다.
- 문서에 "마진 bridge 좋음"이라고 있어도 parser가 위 field로 못 바꾸면 점수는 낮다.

그래서 "연구가 누적됐는데 왜 하닉/삼전 점수가 낮냐"의 답은 다음이다.

- 연구 누적은 배점판을 바꿨다.
- 하지만 연구축을 runtime 입력 field로 바꾸는 번역기는 아직 충분히 바뀌지 않았다.
- Green gate는 낮아지지 않았다.
- 따라서 좋은 연구 사례가 있어도 운영 입력에서 세부 증거가 비면 Green이 막힌다.

## 본 현재 상태

확인한 주요 파일:

- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`
- `data/e2r/calibration/v12/v12_aggregate_metrics.json`
- `data/e2r/calibration/v12/v12_raw_shadow_weight_rows.jsonl`
- `configs/e2r_archetype_weight_profile_v2_2.json`
- `configs/e2r_scoring_profile_v2_2.yaml`
- `reports/e2r_calibration/v12/archetype_weight_runtime_report.md`
- `src/e2r/features.py`
- `src/e2r/scoring.py`
- `src/e2r/staging.py`
- `src/e2r/sector_profiles.py`

## 전체 장부 수치

`v12_trigger_rows_representative.jsonl` 기준:

| 항목 | 값 |
| --- | ---: |
| representative trigger rows | 12,471 |
| unique cases | 9,161 |
| unique symbols | 1,003 |
| current profile error | 6,257 |
| false positive | 3,559 |
| missed structural | 317 |
| too late | 1,680 |
| 4B too early | 122 |
| 4C too late | 281 |
| source_proxy_only | 3,723 |
| evidence_url_pending | 3,906 |
| good Stage2 | 3,329 |
| bad Stage2 | 2,438 |
| Stage2 high MAE | 1,396 |
| Stage2 false positive | 1,978 |
| positive cases | 1,495 |
| counterexamples | 2,628 |
| 4B cases | 2,123 |
| 4C cases | 572 |

해석:

- 연구자료는 "좋은 애를 올려라"만 말한 것이 아니다.
- false positive와 high-MAE 반례도 훨씬 많이 쌓여 있다.
- 그래서 Green 기준을 그냥 낮추면 하닉 같은 winner를 잡는 대신, 반례도 같이 Green으로 올릴 위험이 크다.

## Green은 실제로 있었나

있다.

현재 대표 trigger 파일 기준 `Stage3-Green` 라벨은 `381`개다. 다만 그중 실제 weight calibration에 usable한 Green은 `162`개다. 나머지는 label comparison, 4B/검증용, aggregate 제외 성격이 섞여 있다.

MD 원문 JSON 행 기준:

| 항목 | 값 |
| --- | ---: |
| parsed MD JSON rows | 39,866 |
| score_simulation rows | 9,052 |
| Green-related score_simulation rows | 470 |
| Green score_sim unique keys | 285 |
| all score_sim unique keys | 1,326 |
| runtime scoring field keys in `features.py` | 190 |
| Green score key exact runtime field match | 0 |

중요한 주의:

- exact match가 0이라는 말은 "아무 영향도 없다"는 뜻은 아니다.
- 예를 들어 연구의 `contract_score`는 운영에서 `contract_duration_months`, `contract_amount_to_prior_sales`, `customer_prepayment` 등으로 일부 간접 반영될 수 있다.
- 문제는 연구축 이름 자체가 운영 field로 직접 들어가지 않는다는 것이다.
- 위 `190`은 `features.py`의 `fields.max_*`, `fields.any_bool`, `values_for_scoring` 호출까지 포함해 다시 센 값이다. 이전의 단순 regex 기준보다 넓지만 결론은 같다.

## Green 연구가 본 핵심 증거

대표 Green trigger의 `stage3_evidence_fields` 상위값:

| evidence field | count |
| --- | ---: |
| confirmed_revision | 171 |
| financial_visibility | 169 |
| multiple_public_sources | 154 |
| margin_bridge | 90 |
| low_red_team_risk | 52 |
| durable_customer_confirmation | 38 |
| repeat_order_or_conversion | 22 |

즉 Green은 "테마가 좋다"가 아니다.

연구 Green은 보통 다음 조합이다.

- 실적 또는 revision 확인
- 재무 visibility
- 여러 공개출처
- margin bridge
- 낮은 red-team risk
- 고객/계약/반복수요/상업화 전환

## 운영 scorer가 실제로 읽는 것

운영 scorer는 다음 구조다.

1. `features.py`가 source에서 normalized field를 읽는다.
2. 7개 component를 만든다.
3. `scoring.py`가 archetype별 weight로 7개 component를 재가중한다.
4. `staging.py`가 Green gate를 판정한다.

7개 component:

| component | canonical max |
| --- | ---: |
| eps_fcf_explosion | 20 |
| earnings_visibility | 20 |
| bottleneck_pricing | 20 |
| market_mispricing | 15 |
| valuation_rerating | 15 |
| capital_allocation | 5 |
| information_confidence | 5 |

즉 연구의 `customer_quality_score`, `margin_bridge_score`, `commercialization_score`, `reserve_quality_score`가 별도 component로 runtime에 들어가지 않는다. 결국 7개 component 중 하나로 번역되어야 한다.

## Green gate는 낮아지지 않았다

`configs/e2r_scoring_profile_v2_2.yaml` 기준:

| gate | threshold |
| --- | ---: |
| total | 87 |
| EPS/FCF | 17 |
| visibility | 15 |
| bottleneck | 15 |
| mispricing | 10 |
| valuation | 10 |
| revision | 55 |
| structural visibility | 45 |

그리고 `stage3_green_not_loosened_by_v12: true`다.

쉬운 예:

- C06 weight는 EPS/FCF 24, visibility 21, bottleneck 19로 바뀐다.
- 하지만 Green total 87과 revision/visibility/bottleneck/valuation gate는 그대로다.
- 그래서 "하닉은 HBM이니까 Green"이 아니라, 운영 입력상 모든 gate를 통과해야 한다.

## 주요 아키타입 상태

| archetype | rows | Green | good Stage2 | bad Stage2 | false positive | missed | too late | source proxy | URL pending |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 9 | 82 | 42 | 66 | 11 | 36 | 63 | 78 |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 5 | 116 | 45 | 77 | 18 | 43 | 66 | 50 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 33 | 122 | 43 | 84 | 4 | 77 | 76 | 91 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 37 | 136 | 46 | 78 | 4 | 78 | 100 | 123 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 28 | 91 | 52 | 64 | 7 | 56 | 127 | 134 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 30 | 78 | 45 | 73 | 11 | 62 | 74 | 87 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 14 | 75 | 55 | 90 | 11 | 49 | 105 | 84 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 3 | 58 | 70 | 99 | 15 | 56 | 149 | 156 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 12 | 110 | 105 | 132 | 9 | 60 | 156 | 174 |

해석:

- C06만 문제가 아니다.
- C20, C21, C22, C23처럼 Green 사례가 많은 아키타입도 false positive, too late, source proxy가 같이 많다.
- C30, C31은 Green을 쉽게 열면 바로 policy/PF/event false positive가 커질 가능성이 높다.

## 점수가 실제로 깎이는 위치

### 1. 후보 생성에서 못 들어오는 경우

삼성전자 2024-04-30 replay가 이 경우다.

- stage gate에서 떨어진 것이 아니다.
- `failed_official_cheap_scan`으로 후보 단계에서 빠졌다.

즉 점수 문제 이전에 candidate generation/cheap scan recall 문제가 있다.

### 2. 연구축이 parsed field로 변환되지 않는 경우

연구자료 상위 Green score key:

| research score key | Green score_sim occurrence | runtime parsed field exact match |
| --- | ---: | --- |
| margin_bridge_score | 928 | 없음 |
| relative_strength_score | 920 | 없음 |
| execution_risk_score | 914 | 없음 |
| valuation_repricing_score | 904 | 없음 |
| revision_score | 898 | 없음 |
| contract_score | 896 | 없음 |
| backlog_visibility_score | 896 | 없음 |
| customer_quality_score | 896 | 없음 |
| policy_or_regulatory_score | 886 | 없음 |
| accounting_trust_risk_score | 886 | 없음 |

쉬운 예:

- 연구자료 `customer_quality_score=9`
- 운영 scorer는 `customer_quality_score`를 직접 보지 않는다.
- 대신 `government_customer`, `hyperscaler_customer`, `customer_preorder_or_allocation`, `data_center_contract` 같은 구체 field가 필요하다.

### 3. source eligibility에서 빠지는 경우

`_ParsedFieldSource.values_for_scoring()`은 다음을 score에서 제외한다.

- search snippet only
- search snippet date unverified
- `green_allowed_by_date=false`
- `consensus_proxy_score_eligible=false`
- revision numeric outlier

이 원칙은 맞다. 미래누수와 snippet Green을 막기 위해 필요하다.

하지만 결과적으로 report proxy나 날짜 불확실 자료가 많으면 "사람은 읽을 수 있는 Green 논리"가 운영 score에는 약하게 들어간다.

### 4. proxy consensus/revision이 독립 evidence family로 안 잡히는 경우

`features.py`는 independent consensus/revision과 report-derived proxy를 구분한다.

예:

- report proxy consensus는 점수 일부에는 들어갈 수 있다.
- 하지만 Green family 진단에서는 independent `consensus`, `consensus_revision`이 missing으로 남을 수 있다.

하닉 2024 replay도 이 케이스다.

### 5. 100점 진단축이 20점 component로 압축되는 경우

하닉 C06 예:

| diagnostic | value |
| --- | ---: |
| domain_specific_evidence_score | 80.0000 |
| medium_term_revision_visibility | 100.0000 |
| structural_visibility_quality | 71.3652 |
| sector_bottleneck_score | 51.6040 |
| final bottleneck_pricing | 11.6339 / 20 |

좋은 HBM 진단이 있어도 최종 component로 압축될 때 Green 병목 기준 `15/20`에 못 미친다.

### 6. Green AND gate에서 하나라도 빠지면 막히는 경우

`staging.py`의 Green은 total만 보지 않는다.

Green은 다음을 모두 요구한다.

- total
- EPS/FCF
- visibility
- bottleneck
- mispricing
- valuation
- revision
- structural visibility
- low Red Team risk

쉬운 예:

- EPS/FCF 20점 만점, revision 100점이어도 bottleneck 11.6이면 Green 실패.
- visibility 15.1로 통과해도 total 76.7이면 Green 실패.

## 아키타입별 핵심 문제

### C06 HBM

문제는 HBM 문장을 못 읽는 것만이 아니다. 읽은 HBM 증거가 최종 bottleneck/visibility/component로 충분히 올라가지 못한다.

필요한 패치:

- sold/booked-out capacity -> `capacity_precommitted`, `hbm_capacity_pre_sold`, `hbm_capacity_constraint`
- customer allocation -> `customer_preorder_or_allocation`
- HBM ASP/mix -> `asp_yoy_pct`, `high_margin_mix_improvement`
- Q1 surprise/revision -> `earnings_beat_mentioned`, `estimate_upgrade_mentioned`, numeric revision

### C01/C02/C03 산업재/전력/방산

연구 Green은 backlog, delivery schedule, margin bridge를 본다.

운영은 `contract_amount_to_prior_sales`, `order_backlog_to_sales`, `record_backlog`, `contract_duration_months` 같은 숫자/boolean이 필요하다.

문제:

- "수주잔고 좋음" 문장이 숫자/field로 안 바뀌면 visibility가 약하다.
- 전력/방산은 contract gate가 있어 false positive를 막지만, 좋은 케이스도 field 부족이면 Green이 막힌다.

### C20 소비재 수출

연구 Green은 export channel, reorder, repeat demand, margin bridge를 본다.

운영은 K-food/K-beauty sector profile이 있지만, 핵심은 여전히 다음 field 변환이다.

- `export_ratio`
- `export_growth_pct`
- `export_channel_expansion`
- `overseas_channel_expansion`
- `recurring_consumer_demand`
- `opm_expansion_pctp`

문제:

- "올리브영/아마존/미국 채널 확대" 같은 말이 channel field로 안 바뀌면 Green 근거가 약해진다.

### C21/C22 금융/보험

연구 Green은 ROE/PBR, capital return, reserve/rate cycle을 본다.

하지만 runtime sector profile에는 금융/보험 전용 `SectorProfile`이 없다. archetype weight는 valuation/capital을 크게 주지만, feature extractor는 generic 경로를 많이 탄다.

문제:

- `roe_pbr_capital_return_score`, `reserve_quality_score`, `kics_capital_buffer_score`, `shareholder_return_visibility_score`가 운영 parsed field로 직접 들어가지 않는다.

### C23/C24/C25 바이오/헬스케어

연구 Green은 approval, commercialization, royalty/revenue conversion, reimbursement/export conversion을 본다.

runtime sector profile에는 bio 전용 프로필이 없다. classification은 C23/C24/C25로 갈 수 있지만 feature extraction은 generic component로 압축된다.

문제:

- `commercialization_score`, `product_route_score`, `source_quality_score`가 direct runtime field가 아니다.
- approval headline만 Green으로 열면 false positive 위험이 있으므로 revenue/royalty conversion field가 필요하다.

### C26/C27/C28 플랫폼/콘텐츠/보안

연구 Green은 ARPU, monetization, ARR/retention, margin leverage를 본다.

runtime에는 `AI_INFRA_PLATFORM`은 있지만 SaaS/security/content 전용 sector profile은 없다.

문제:

- `arr_retention`, `net_revenue_retention`, `security_contract_retention`, `ad_revenue_operating_leverage` 같은 세부 field 매핑이 부족하면 C28/C26 Green이 약해진다.

### C30/C31/R13 보호형 아키타입

이쪽은 Green을 여는 것보다 잘 막는 것이 중요하다.

연구자료는 high-MAE, false positive, 4B/4C를 많이 쌓았다.

문제:

- positive bridge를 너무 느슨하게 열면 policy/PF/event headline이 Stage2/Green으로 올라간다.
- 그래서 Green 완화가 아니라 "cashflow/PF/legal/margin bridge가 있을 때만 positive"가 필요하다.

## 왜 하닉 같은 obvious winner도 못 잡나

하닉은 C06에서 다음 연구축이 필요하다.

- HBM customer capacity
- sold/booked-out capacity
- Q1 surprise
- multi-quarter revision
- ASP/mix improvement
- financial visibility

현재 runtime은 일부를 읽는다.

- HBM demand
- memory price increase
- supply discipline
- customer allocation
- advanced packaging bottleneck

하지만 최종 Green에는 더 필요하다.

- numeric revision 또는 estimate upgrade
- independent consensus/revision family
- actual OP/FCF bridge
- bottleneck component 15 이상
- total 87 이상

그래서 하닉은 연구 정답표상 Green이어도, 운영 replay에서는 Yellow 76.7639에 머문다.

## 현재 구조의 한 문장 요약

연구자료는 "무엇이 Green인지"를 많이 배웠지만, 운영 파이프라인은 아직 "그 Green 논리를 source-backed normalized field로 읽어 점수화하는 법"을 충분히 배우지 못했다.

쉬운 예:

- 연구자료는 의사가 쓴 진단서다.
- 운영 scorer는 체크박스 기계다.
- 진단서에 "상태 매우 좋음"이라고 적혀 있어도, 체크박스의 `혈압`, `체온`, `검사수치` 칸이 비면 기계는 높은 점수를 못 준다.

## 다음 작업 우선순위

1. Research axis -> runtime field mapping table 작성
   - Green score key 285개를 runtime scoring field 190개에 semantic mapping한다.
   - exact match가 아니라 `margin_bridge_score -> opm_expansion_pctp / actual_op_yoy_pct / fy2_op growth / fcf_growth_pct` 같은 변환표가 필요하다.

2. 대표 Green replay fixture 만들기
   - C06 SK하이닉스 2024-04-26
   - C02 HD현대일렉
   - C20 K-food/K-beauty
   - C21/C22 금융/보험
   - C23 바이오 approval commercialization
   - C28 security/SaaS

3. Parser/feature patch
   - 문장형 evidence를 normalized field로 바꾸는 parser 개선.
   - 단 deterministic fallback query를 늘리는 방식은 금지.

4. Green recall 패치 후 false-positive replay
   - R13, C30, C31, C14, C17 같은 high-MAE/guardrail archetype이 같이 뚫리지 않는지 확인한다.

5. Candidate generation audit
   - 삼성전자 2024-04-30처럼 scoring 전에 `failed_official_cheap_scan`으로 빠지는 케이스를 별도 점검한다.

## 지금 결론

HBM 리포트 신호 변환부만 고치면 끝나는 문제가 아니다.

하닉 C06은 가장 잘 보이는 증상이다. 전체적으로는 다음 4개가 같이 문제다.

1. candidate generation recall
2. research-axis to runtime-field translation
3. source/proxy confidence handling
4. Green gate와 false-positive guard의 균형

따라서 다음 패치는 "Green threshold 완화"가 아니라 "연구축을 운영 field로 정확히 번역하고, 대표 Green/false-positive replay로 검증"해야 한다.
