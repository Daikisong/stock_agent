# Runtime Conversion Root Cause Audit - 2026-06-19

## 결론

삼전/하닉 점수가 낮은 이유는 HBM 전망을 몰라서가 아니다.

누적 연구는 들어와 있다. 특히 V12 연구자료는 Stage3-Green, Stage2-Actionable, false-positive, 4B/4C 반례를 많이 담고 있고, 일부는 runtime weight profile에도 반영됐다.

문제는 그 다음 층이다.

```text
누적 연구자료
-> archetype별 weight/gate 후보
-> runtime weight profile 일부 반영
-> source text parser
-> runtime primitive field
-> feature adapter/sub-score
-> 7개 component
-> Stage3-Green AND gate
```

현재 병목은 `weight`가 아니라 `source text -> runtime primitive -> component` 변환이다.

쉬운 예:

- 연구 누적 결과: "C06 HBM은 EPS/visibility/bottleneck 비중을 높게 봐야 한다."
- 실제 runtime: C06 weight는 이미 `24/21/19/15/12/4/5`로 바뀌어 있다.
- 그런데 보고서 문장에서 `HBM CAPA 제약`, `advanced packaging bottleneck`이 `hbm_capacity_constraint`, `advanced_packaging_bottleneck` field로 안 바뀌면, 커진 bottleneck 배점에 들어갈 원재료가 없다.

시험으로 치면, 배점표는 맞게 바뀌었는데 답안지 해당 칸이 빈칸으로 들어가는 상황이다.

## 확인한 근거

### 1. 누적 연구자료는 Green을 이미 포함한다

파일:

- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`
- `data/e2r/calibration/v12/v12_raw_shadow_weight_rows.jsonl`
- `configs/e2r_archetype_weight_profile_v2_2.json`

대표 수치:

| 항목 | 값 |
| --- | ---: |
| representative trigger rows | 12,471 |
| Stage3-Green rows | 381 |
| Stage2-Actionable rows | 4,704 |
| current_profile_too_late rows | 473 |
| current_profile_missed_structural rows | 213 |

아키타입별 예:

| archetype | rows | Stage3-Green | Stage2-Actionable | 의미 |
| --- | ---: | ---: | ---: | --- |
| C06 HBM memory | 229 | 9 | 92 | 하닉 같은 HBM 구조 성공/반례가 이미 있음 |
| C21 financial | 413 | 37 | 196 | 저PBR/ROE/자본환원 사례가 있음 |
| C22 insurance | 327 | 28 | 145 | CSM/IFRS17/자본여력 사례가 있음 |
| C23 bio approval | 269 | 30 | 100 | 승인 이후 매출/로열티 전환 사례가 있음 |
| C28 software/security | 285 | 14 | 91 | ARR/retention/계약 전환 사례가 있음 |

즉 "예전에 Green으로 갈 만한 애들이 연구에 없었다"가 아니다. 있다.

### 2. runtime weight는 실제로 반영됐다

`configs/e2r_archetype_weight_profile_v2_2.json` 기준:

| archetype | green_policy | runtime weights |
| --- | --- | --- |
| C06 | `green_allowed_with_hbm_capacity_customer_and_revision` | `24/21/19/15/12/4/5` |
| C21 | `green_allowed_with_roe_pbr_and_executed_capital_return` | `15/20/5/15/25/15/5` |
| C22 | `green_allowed_with_reserve_rate_cycle_and_capital_return` | `12/22/5/14/24/18/5` |
| C23 | `watch_to_green_after_approval_revenue_or_royalty_conversion` | `12/24/5/12/10/7/30` |
| C28 | `green_allowed_with_arr_retention_and_margin_leverage` | `20/24/8/16/14/8/10` |

따라서 "연구가 아예 점수표에 반영되지 않았다"는 표현은 반만 맞다.

맞는 표현:

- 아키타입별 배점표는 누적 연구로 반영됐다.
- 하지만 연구축을 runtime primitive로 번역하는 field layer는 충분히 반영되지 않았다.

### 3. 현재 Green gate는 모든 후보를 막고 있다

파일:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv`

120개 benchmark replay 결과:

| stage | count |
| --- | ---: |
| Stage3-Green | 0 |
| Stage3-Yellow | 12 |
| Stage2 | 34 |
| Stage1 | 67 |
| Stage0 | 7 |

반복 실패 gate:

| gate | fail count / 120 |
| --- | ---: |
| `failed_stage3_total_score` | 120 |
| `failed_stage3_bottleneck` | 120 |
| `failed_stage3_visibility` | 98 |
| `failed_stage3_valuation` | 78 |
| `failed_stage3_market_mispricing` | 67 |
| `failed_stage3_revision` | 56 |
| `failed_sector_bottleneck` | 56 |
| `failed_structural_visibility_quality` | 44 |

이건 특정 HBM 문제가 아니라 전역 Green 변환 문제다.

### 4. HBM 사례의 실제 score loss

파일:

- `data/report_snapshots/sk_hynix_memory_20240401.txt`
- `data/report_snapshots/samsung_memory_20240401.txt`
- `src/e2r/research/report_parser.py`
- `src/e2r/features.py`

스냅샷 문장:

```text
advanced packaging bottleneck과 HBM CAPA 제약이 공급 병목으로 언급된다.
```

현재 parser 출력:

| field | SK hynix parsed | Samsung parsed |
| --- | --- | --- |
| `hbm_demand_mentioned` | true | true |
| `memory_price_increase_mentioned` | true | true |
| `supply_discipline_mentioned` | true | true |
| `customer_preorder_or_allocation` | true | null |
| `capacity_precommitted` | null | null |
| `hbm_capacity_pre_sold` | null | null |
| `capacity_constraint` | null | null |
| `capa_shortage` | null | null |
| `hbm_capacity_constraint` | null | null |
| `advanced_packaging_bottleneck` | null | null |

즉 문장은 있는데 field가 비어 있다.

report-only feature/scoring:

| symbol | eps | visibility | bottleneck | mispricing | valuation | weighted total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SK hynix base | 15.00 | 11.29 | 8.63 | 11.65 | 10.39 | 58.76 |
| SK hynix forced CAPA fields | 15.00 | 12.58 | 10.55 | 11.77 | 10.48 | 62.93 |
| Samsung base | 10.50 | 9.48 | 7.44 | 10.40 | 9.75 | 48.56 |
| Samsung forced CAPA fields | 10.50 | 11.21 | 10.38 | 10.52 | 9.84 | 54.16 |

해석:

- parser 누락은 분명히 있다.
- 하지만 CAPA field만 켜도 Green까지는 못 간다.
- 그러므로 "HBM 토큰 몇 개 추가"는 필요한 최소 패치일 뿐, 최종 해결은 아니다.

### 5. 운영 replay의 하닉/삼성 loss

파일:

- `output/0619_asof_replay_hbm_2024_04_25/2024-04-25_to_2024-04-25/discovered_candidates.csv`

2024-04-25 as-of replay:

| symbol | stage | total | eps | visibility | bottleneck | mispricing | valuation | confidence |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SK hynix | 3-Yellow | 76.0596 | 20.00 | 14.7057 | 11.3960 | 12.8520 | 12.3390 | 3.0 |
| Samsung | 2 | 68.6752 | 20.00 | 12.4403 | 9.9143 | 11.5980 | 11.6985 | 3.0 |

Green gate는 AND 구조다.

`src/e2r/staging.py` 기준:

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

하닉은 EPS, mispricing, valuation은 통과에 가깝거나 통과한다. 하지만 visibility가 15 바로 아래이고 bottleneck은 11.4라서 닫힌다.

삼성은 visibility/bottleneck이 더 낮다. 이건 "삼성도 무조건 Green이어야 한다"는 뜻이 아니라, catch-up HBM과 구조적 leader HBM을 가르는 primitive가 더 정밀해야 한다는 뜻이다.

쉬운 예:

- 하닉 positive: 고객 lock + CAPA lock + ASP + revision + FCF bridge가 같이 있어야 한다.
- 삼성 guard: HBM catch-up, qualification 지연, 공급계약 미확정이면 Green을 막아야 한다.

둘 다 HBM 전용 보너스가 아니라 positive/guard 쌍으로 테스트해야 한다.

## 전체 아키타입으로 일반화한 문제

### sector profile이 36개 archetype을 다 표현하지 못한다

현재 `src/e2r/sector_profiles.py`의 runtime sector profile은 9개다.

```text
POWER_EQUIPMENT
DEFENSE
K_FOOD_EXPORT
K_BEAUTY_EXPORT
MEMORY_HBM
CYCLICAL_SHIPPING
BATTERY_OVERHEAT
AI_INFRA_PLATFORM
GENERIC
```

하지만 V12 canonical archetype은 36개다.

문제:

- C21 금융은 `roe/pbr/buyback/dividend/credit_cost` 중심이어야 한다.
- C22 보험은 `CSM/K-ICS/reserve/loss ratio` 중심이어야 한다.
- C23 바이오는 `approval_to_revenue/royalty/reimbursement` 중심이어야 한다.
- C28 소프트웨어는 `ARR/RPO/retention/churn/renewal` 중심이어야 한다.

현재 parser/features에서 이 필드들은 거의 없다.

`rg` 확인 결과:

- `report_parser.py`, `features.py`, `sector_profiles.py`에 `csm`, `k_ics`, `solvency`, `loss_ratio`, `regulatory_approval`, `approval_to_revenue`, `royalty`, `arr_growth`, `retention`, `churn`, `nrr`, `renewal` 같은 runtime primitive가 거의 없다.
- 일부 단어는 `archetype_classifier.py`에서 분류용으로만 쓰인다.
- 분류용 단어와 점수용 primitive는 다르다.

쉬운 예:

- 분류: "이건 보험이다"라고 알아보는 단계.
- 점수: "CSM이 얼마나 늘고, 지급여력/K-ICS가 충분하고, reserve risk가 낮은가"를 수치/field로 반영하는 단계.

현재는 후자가 비어 있다.

### benchmark 평균도 같은 현상을 보인다

`score_components_by_candidate.csv` 기준:

| sector_profile | n | avg score | avg EPS | avg visibility | avg bottleneck | avg contract | avg backlog | avg CAPA | avg domain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MEMORY_HBM | 20 | 74.90 | 20.00 | 14.78 | 10.82 | 0.00 | 14.25 | 0.00 | 79.00 |
| POWER_EQUIPMENT | 48 | 58.36 | 17.88 | 11.38 | 8.05 | 21.20 | 51.56 | 32.43 | 37.12 |
| K_BEAUTY_EXPORT | 11 | 50.09 | 9.00 | 11.66 | 9.36 | 35.00 | 0.00 | 0.00 | 96.00 |
| DEFENSE | 12 | 29.40 | 0.00 | 10.64 | 2.80 | 62.00 | 70.00 | 0.00 | 40.00 |
| GENERIC | 29 | 26.30 | 7.59 | 5.06 | 2.37 | 13.28 | 0.00 | 0.00 | 5.31 |

핵심:

- MEMORY_HBM은 domain evidence와 EPS는 높은데 CAPA가 0이고 bottleneck이 15에 못 간다.
- POWER_EQUIPMENT는 backlog는 있는데 bottleneck/visibility 변환이 약하다.
- DEFENSE는 계약/backlog가 있는데 EPS/FCF와 CAPA 연결이 약하다.
- GENERIC은 대부분 아키타입별 primitive가 없어서 거의 빈 점수판이다.

## 그래서 기존 작업이 "전부 잘못"은 아니지만 "불완전"하다

맞게 된 부분:

1. V12 연구자료는 누적 장부에 쌓였다.
2. 대표 row와 shadow weight가 생성됐다.
3. runtime archetype weight profile이 만들어졌고 scoring에 적용된다.
4. Green threshold는 무리하게 낮추지 않았다.

잘못되거나 부족한 부분:

1. 연구축을 runtime field로 옮기는 EvidenceBridge가 부족하다.
2. parser가 domain phrase를 너무 좁게 잡는다.
3. 36개 archetype을 9개 sector profile로 압축해 feature adapter가 부족하다.
4. Stage 실패 설명이 `failed_stage3_bottleneck` 같은 최종 gate만 보여주고, 어떤 연구축이 어떤 field에서 0점이 됐는지 보여주지 않는다.
5. positive fixture와 guard fixture를 한 쌍으로 검증하는 테스트가 아직 없다.

## 바로 고쳐야 할 순서

1. HBM parser 최소 패치
   - `HBM CAPA 제약`
   - `advanced packaging bottleneck`
   - `CoWoS bottleneck`
   - `packaging capacity allocated`
   - `customer qualification`
   - `no supply deal`, `partial pass`

2. EvidenceBridgeSpec 구현
   - `margin_bridge_score`
   - `customer_quality_score`
   - `backlog_visibility_score`
   - `contract_score`
   - `policy_or_regulatory_score`
   - `accounting_trust_risk_score`

3. non-HBM primitive 추가
   - C21: `roe_pbr_gap_score`, `buyback_executed`, `treasury_share_cancellation`, `dividend_growth_visible`, `credit_cost_quality`
   - C22: `csm_growth`, `k_ics_ratio`, `reserve_quality_score`, `loss_ratio_quality`
   - C23/C25: `regulatory_approval_confirmed`, `approval_to_revenue_bridge`, `royalty_route`, `reimbursement_confirmed`
   - C28: `arr_growth`, `rpo_to_sales`, `retention_or_renewal`, `nrr`, `churn_low`

4. archetype adapter 추가
   - sector profile 9개만 쓰지 말고 canonical archetype별 adapter를 둔다.
   - 단, 최종 score/stage는 deterministic rule engine이 계산한다.

5. score loss report 추가
   - 현재: `failed_stage3_bottleneck`
   - 필요: `research_axis=HBM_capacity_lock`, `expected=hbm_capacity_constraint`, `observed=null`, `lost_component=bottleneck_pricing`

6. positive/guard fixture 테스트
   - 하닉 positive와 삼성 catch-up guard를 한 쌍으로 둔다.
   - C21/C22/C23/C28도 같은 방식으로 둔다.

## 한 줄 답

삼전/하닉이 낮게 나온 건 누적 연구가 없어서가 아니다.

누적 연구는 weight와 장부에는 반영됐지만, source-backed evidence를 runtime primitive로 바꾸는 층이 부족해서 실제 score component까지 못 올라간다. 이 문제는 HBM만의 문제가 아니라 C21 금융, C22 보험, C23 바이오, C28 소프트웨어 등 전체 아키타입에서 반복될 구조적 문제다.
