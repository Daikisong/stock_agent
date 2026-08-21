# E2R v5 Operational Acceptance & Verifiable Market Cutover Master Goal v6
## Phase 101–109 — Tracked Score Receipts / Clean-Clone Reproduction / Cross-Archetype Live Canaries / Real KRX Census / Operational Cutover

너는 `Daikisong/stock_agent`의 수석 아키텍트·운영 검증 책임자다.

이번 Goal은 또 다른 대규모 scoring architecture를 새로 만드는 작업이 아니다.

현재 v5 Researcher Mode의 핵심 구조를 **동결해서 보존**한 채, 다음 네 가지를 실제 운영 수준으로 완결하는 작업이다.

```text
1. 삼성전자·SK하이닉스의 실제 component 점수와 Stage를
   GitHub에서 독립 검수할 수 있는 compact receipt로 커밋한다.

2. output/, 로컬 cache, 협업 journal, 절대경로가 없는 clean clone에서도
   receipt만으로 점수·Stage·Gold recall·readiness를 재검산한다.

3. C06 외 C08/C15/C17/C24/C28을 실제 current source로 각각 최소 1종목씩
   Researcher Mode 전체 경로로 실행해 일반화를 증명한다.

4. 최신 실제 KRX universe로 daily/Census selective-deep 운영을 1회 수행하고,
   실제 후보 선정→연구→점수→Stage까지 연결된 운영 산출물을 커밋한다.
```

최종 목표는 다음 한 문장이다.

```text
Researcher Mode가 두 canary에서만 동작하는 연구실 엔진이 아니라,
깨끗한 checkout에서 재검산 가능하고,
여러 아키타입과 실제 KRX Census에서 동작하는 운영 시스템임을 증명하라.
```

---

# 0. 시작 상태를 신뢰하지 말고 직접 재검산하라

현재 보고상 다음 상태다.

```text
HEAD: 2e3d2c97...
engine verdict: MEANINGFUL_E2R_RESEARCHER_PARITY_READY
삼성전자: 7/7 memo, score_valid=true, FINAL StageCourt=true
SK하이닉스: 7/7 memo, score_valid=true, FINAL StageCourt=true
Gold post-run recall: PASS
full tests: 6,637 PASS
Reviewer A~J: PASS
```

그러나 이것을 그대로 전제하지 마라.

첫 작업으로 반드시:

```text
git rev-parse HEAD
git rev-parse origin/main
git status --short
현재 readiness 재컴파일
현재 Reviewer A~J 재실행
현재 full-test receipt 검증
```

을 수행하고 시작 commit과 tree hash를 기록하라.

현재 알려진 핵심 미완료는 다음이다.

```text
- 실제 7개 component 점수와 total score, canonical Stage가 tracked docs에 없음
- 실제 score/stage leaf가 output/ 아래에 있고 output/은 gitignore 대상
- clean clone에서 현재 final readiness를 독립 재현하기 어려움
- self-repair snapshot과 final StageCourt 문서 사이에 시점 불일치가 존재할 수 있음
- production status에 PENDING_POST_RUN_GOLD 문자열이 남아 운영자가 오해할 수 있음
- daily/Census integration은 synthetic target 중심이며 실제 current KRX 실전 run이 아님
- C06 외 current live Researcher Mode canary가 없음
```

이번 Goal은 정확히 이 공백만 해결한다.

---

# 1. 절대 보존할 v5 canonical architecture

다음은 변경하거나 되돌리지 마라.

```text
Historical Research Judgment Atlas
Component Anchor Atlas
Researcher Mode
Evidence Fact Graph
Analyst / Skeptic / Calibration Judge
Deterministic Score Aggregator
Deterministic StageCourt
Gold lane post-run isolation
Question/primitive의 score authority 제거
LLM query-generation authority
source-backed claim lineage
counter/supersession 처리
```

특히 다음 회귀를 금지한다.

```text
- QuestionImpactContract를 다시 score gate로 승격
- exact primitive 미발견을 component 0점으로 처리
- keyword match를 scoring authority로 사용
- fixed query template로 회귀
- LLM이 total score 또는 canonical Stage 직접 출력
- Gold query/URL/fact를 Production에 주입
- provider failure를 낮은 score로 확정
- fixed round/query/document count를 research completion으로 사용
- 삼성전자·SK하이닉스 또는 특정 symbol 분기
- expected score나 expected Stage 하드코딩
```

---

# 2. 이번 Goal의 정확한 범위

## 포함

```text
- tracked compact receipts
- 실제 점수와 Stage 공개
- receipt-only deterministic recomputation
- clean clone verification
- artifact lifecycle 정리
- current cross-archetype live canary
- current real KRX Census selective-deep
- one-command operational acceptance
- CI/offline verification
- 독립 reviewer
```

## 제외

```text
- 새로운 scoring 철학 재설계
- 7개 component weight 임의 변경
- 삼성·하이닉스 점수 목표값 강제
- 모든 KRX 종목을 매일 L5 full research
- 자동 매매
- 추천 문구 출력
- raw 300MB checkpoint 전체 Git 커밋
- secret/API key 커밋
```

---

# 3. 최종 디렉터리 계약

다음 tracked artifact root를 만든다.

```text
docs/operational/e2r_v6_operational_cutover/
```

필수 구조:

```text
docs/operational/e2r_v6_operational_cutover/
├── README.md
├── starting_state.json
├── artifact_lifecycle_audit.json
├── clean_clone_reproduction.json
├── provider_runtime_audit.json
├── cross_archetype_canary_selection.json
├── cross_archetype_canary_summary.json
├── current_krx_census_summary.json
├── current_krx_stage_map_compact.jsonl
├── operational_acceptance_reviewer_gate.json
├── operational_cutover_final.md
├── canary_receipts/
│   └── 2026-07-12/
│       ├── 005930/
│       │   ├── receipt_manifest.json
│       │   ├── score_receipt.json
│       │   ├── component_decisions.jsonl
│       │   ├── scoring_facts.jsonl
│       │   ├── judge_decisions.jsonl
│       │   ├── source_manifest.jsonl
│       │   └── stagecourt_receipt.json
│       └── 000660/
│           └── ...
├── current_live_canaries/
│   ├── C08_.../
│   ├── C15_.../
│   ├── C17_.../
│   ├── C24_.../
│   └── C28_.../
└── clean_clone/
    ├── receipt_recompute_result.json
    ├── tracked_readiness_result.json
    └── test_result.json
```

raw full corpus는 계속 `output/` 또는 cache에 둔다.

Git에는 **최종 판단을 독립 검수하는 데 필요한 최소 완전 receipt만** 커밋한다.

---

# 4. Tracked Receipt 원칙

Tracked receipt는 단순 summary가 아니다.

다음 질문에 답할 수 있어야 한다.

```text
- 최종 점수는 몇 점인가
- 7개 component 각각 몇 점인가
- 각 component 최대점은 몇 점인가
- 어떤 positive fact가 점수에 들어갔는가
- 어떤 counterfact가 점수를 낮췄는가
- 어떤 historical anchor와 비교했는가
- Analyst/Skeptic/Calibration Judge가 각각 무엇을 제안했는가
- deterministic aggregator가 어떻게 최종 component 점수를 정했는가
- StageCourt가 어떤 입력으로 어떤 Stage를 냈는가
- 이 결과가 어떤 code/config/prompt/provider/corpus hash에서 나왔는가
```

다음은 receipt가 아니다.

```text
score_valid=true
stage_final=true
7/7 complete
```

실제 숫자와 lineage가 없으면 FAIL이다.

---

# 5. 필수 Schema

## 5.1 ReceiptManifest

```json
{
  "schema_version": "e2r_v6_tracked_receipt_manifest_v1",
  "receipt_id": "...",
  "target_id": "005930",
  "company_name": "삼성전자",
  "as_of_date": "2026-07-12",
  "latest_trading_snapshot_date": "2026-07-10",
  "archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "run_commit_sha": "...",
  "verification_commit_sha": "...",
  "config_hash": "...",
  "prompt_hashes": {},
  "provider_identity_hash": "...",
  "source_corpus_hash": "...",
  "output_tree_hash": "...",
  "tracked_receipt_tree_hash": "...",
  "gold_visible_during_production": false,
  "provider_selected_explicitly": true,
  "provider_route": "COLLABORATION_CODEX_SUBAGENT",
  "qwen_call_count": 0,
  "ollama_call_count": 0,
  "score_or_stage_authority": false
}
```

## 5.2 ScoreReceipt

```json
{
  "schema_version": "e2r_v6_score_receipt_v1",
  "target_id": "...",
  "score_scale": "FULL_E2R_100",
  "score_valid": true,
  "component_score_vector": {
    "eps_fcf_explosion": 0.0,
    "earnings_visibility": 0.0,
    "bottleneck_pricing": 0.0,
    "market_mispricing": 0.0,
    "valuation_rerating": 0.0,
    "capital_allocation": 0.0,
    "information_confidence": 0.0
  },
  "component_max_vector": {},
  "total_score": 0.0,
  "total_score_recomputed": 0.0,
  "component_sum_matches_total": true,
  "research_complete": true,
  "semantic_saturation_certified": true,
  "material_gap_count": 0,
  "provider_error_count": 0,
  "canonical_stage": "...",
  "stage_status": "FINAL",
  "risk_overlay": "...",
  "hard_break_fact_ids": [],
  "daily_event_overlay_can_change_canonical_stage": false
}
```

## 5.3 ComponentDecisionReceipt

```json
{
  "component_id": "...",
  "max_points": 0.0,
  "final_points": 0.0,
  "support_fact_ids": [],
  "counter_fact_ids": [],
  "resolution_fact_ids": [],
  "historical_anchor_ids": [],
  "judge_decision_ids": [],
  "why_not_higher": "...",
  "why_not_lower": "...",
  "confidence": 0.0,
  "research_status": "RESEARCH_COMPLETE",
  "aggregation_method": "...",
  "aggregation_trace_hash": "..."
}
```

## 5.4 ScoringFactReceipt

모든 **최종 점수 또는 Stage에 실제 사용된** support/counter/resolution/hard-break fact를 포함한다.

```json
{
  "fact_id": "...",
  "target_id": "...",
  "component_ids": [],
  "fact_role": "SUPPORT|COUNTER|RESOLUTION|HARD_BREAK",
  "subject_id": "...",
  "business_segment": "...",
  "product_family": "...",
  "economic_mechanism": "...",
  "predicate_family": "...",
  "normalized_object": "...",
  "value": null,
  "unit": null,
  "period": "...",
  "temporal_status": "CURRENT",
  "source_url": "...",
  "source_title": "...",
  "source_publisher": "...",
  "source_tier": "...",
  "published_at": "...",
  "available_at": "...",
  "document_content_hash": "...",
  "exact_quote_hash": "...",
  "quote_excerpt": "...",
  "page_section_locator": "...",
  "issuer_scoped": true,
  "current_score_eligible": true,
  "source_independence_group": "..."
}
```

`quote_excerpt`는 검수 가능한 짧은 길이로 제한한다.
raw 문서 전체를 커밋하지 않는다.

## 5.5 JudgeDecisionReceipt

```json
{
  "judge_decision_id": "...",
  "component_id": "...",
  "role": "ANALYST|SKEPTIC|CALIBRATION_JUDGE",
  "proposed_points": 0.0,
  "allowed_range": [0.0, 0.0],
  "support_fact_ids": [],
  "counter_fact_ids": [],
  "anchor_ids": [],
  "why_higher": "...",
  "why_lower": "...",
  "prompt_hash": "...",
  "provider_call_id": "...",
  "score_or_stage_authority": false
}
```

## 5.6 StageCourtReceipt

```json
{
  "schema_version": "e2r_v6_stagecourt_receipt_v1",
  "target_id": "...",
  "score_receipt_id": "...",
  "component_score_vector_hash": "...",
  "total_score": 0.0,
  "risk_fact_ids": [],
  "hard_break_fact_ids": [],
  "canonical_stage": "...",
  "decision_status": "FINAL",
  "score_valid": true,
  "event_overlay": "...",
  "event_overlay_changed_canonical_stage": false,
  "stagecourt_rule_hash": "...",
  "decision_trace_hash": "..."
}
```

---

# 6. Phase 101 — 삼성·하이닉스 Tracked Score Receipt

현재 로컬 `output/researcher_mode/...`의 canonical leaf를 읽어
삼성전자와 SK하이닉스 receipt를 만든다.

## 반드시 포함할 값

```text
- 실제 7개 component 점수
- 실제 component max
- 실제 total score
- 실제 canonical Stage
- Stage final status
- 모든 score-bearing support fact
- 모든 score-bearing counterfact
- hard-break/risk fact
- judge decisions
- historical anchor IDs
- provider identity/call counts
- query/document/fact/counterfact counts
- output tree hash
- Gold post-run comparison metrics
```

## 금지

```text
- 점수 숫자 생략
- Stage 숫자 생략
- receipt에 score_valid=true만 기록
- top 3 fact만 기록하고 나머지 scored fact 누락
- output/ 경로가 없으면 verifier가 작동하지 않는 구조
- Gold fact를 current score fact처럼 receipt에 포함
- absolute /root/... path를 portable identity로 사용
```

## Portable reviewer identity

기존 artifact에 `/root/...` 같은 실행환경 절대경로가 reviewer identity로 남아 있다면 제거한다.

새 identity 예:

```text
CODEX_POST_RUN_PRIMARY
CODEX_POST_RUN_REVIEWER_A
CODEX_POST_RUN_REVIEWER_B
```

identity는:

```text
role_id
provider_route
provider_call_id
prompt_hash
response_hash
```

로 검증한다.

filesystem username/path에 의존하지 않는다.

## 신규 CLI

```bash
PYTHONPATH=src python -m e2r.cli.export_e2r_v6_tracked_receipts \
  --repo-root . \
  --source-output-root output/researcher_mode/c06/2026-07-12 \
  --targets 005930,000660 \
  --destination docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12
```

## Hard acceptance

```text
target receipt count = 2
missing component score count = 0
missing total score count = 0
missing canonical Stage count = 0
missing scored fact lineage count = 0
orphan fact id count = 0
orphan judge id count = 0
orphan anchor id count = 0
component sum mismatch count = 0
stage score mismatch count = 0
Gold leakage count = 0
absolute path identity count = 0
qwen call count = 0
ollama call count = 0
```

커밋:

```text
Phase 101 삼성·하이닉스 실제 점수·Stage 검수 receipt를 공개하다
```

---

# 7. Phase 102 — Receipt-Only Deterministic Reproduction

새 verifier를 만든다.

```bash
PYTHONPATH=src python -m e2r.cli.verify_e2r_v6_tracked_receipts \
  --receipt-root docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12 \
  --offline true
```

verifier는 다음만 사용한다.

```text
tracked receipt
current source code
current config
```

다음을 읽으면 FAIL이다.

```text
output/
data/cache/
~/.cache/
협업 journal
.env
로컬 provider response cache
절대경로 artifact
untracked file
```

## verifier가 재계산할 것

```text
- 7개 component roster
- component points 범위
- component sum
- total score
- score scale
- score_valid
- hard-break eligibility
- deterministic canonical Stage
- receipt tree hash
- source/judge/anchor referential integrity
- Gold leakage absence
```

## output tree와 receipt 관계

receipt는 원본 output tree hash를 보존하지만,
검증 실행은 output tree가 없어도 통과해야 한다.

```text
origin output:
historical provenance

tracked receipt:
portable verification source
```

둘을 구분한다.

## Tamper tests

다음 각각은 verifier를 실패시켜야 한다.

```text
- component 점수 0.1 변경
- total score 변경
- canonical Stage 변경
- support fact 삭제
- counter fact 삭제
- fact source URL 변경
- quote hash 변경
- judge decision 삭제
- anchor ID 삭제
- Gold fact 삽입
- Qwen provider identity로 변경
```

커밋:

```text
Phase 102 output 없이 receipt만으로 점수·Stage 재현을 완성하다
```

---

# 8. Phase 103 — Clean Clone Reproduction

임시 디렉터리에 **origin/main의 깨끗한 clone**을 만든다.

최종 push 전에는 임시 worktree로 예비검증하고,
최종 push 후에는 반드시 origin/main을 다시 clone해 최종검증한다.

예:

```bash
TMP="$(mktemp -d)"
git clone --no-local <origin-url> "$TMP/stock_agent"
cd "$TMP/stock_agent"
git checkout <final-sha>
test -z "$(git status --porcelain)"
test ! -d output
test ! -f .env
PYTHONPATH=src python -m e2r.cli.verify_e2r_v6_tracked_receipts ...
PYTHONPATH=src python -m e2r.cli.compile_e2r_v6_tracked_readiness ...
python -m unittest discover -s tests -v
```

## Clean clone acceptance

```text
output directory absent = true
.env absent = true
local provider journal absent = true
tracked receipt verification = PASS
tracked readiness = PASS
score/stage values equal original run = true
same receipt replay variance = 0
full tests = PASS
verification tree stable = true
```

## 필수 artifact

```text
docs/operational/e2r_v6_operational_cutover/clean_clone_reproduction.json
docs/operational/e2r_v6_operational_cutover/clean_clone/receipt_recompute_result.json
docs/operational/e2r_v6_operational_cutover/clean_clone/tracked_readiness_result.json
docs/operational/e2r_v6_operational_cutover/clean_clone/test_result.json
```

커밋:

```text
Phase 103 origin main clean clone 독립 재현을 증명하다
```

---

# 9. Phase 104 — Artifact Lifecycle와 상태 정합성

현재 문서 사이의 시점 불일치를 제거한다.

## 상태 분리

다음처럼 기록한다.

```text
production_research_status = COMPLETE
gold_evaluation_status = PASS
score_status = COMPLETE
stagecourt_status = FINAL
```

다음 문자열을 최종 사용자 문서에서 completion status로 쓰지 않는다.

```text
PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD
```

Production lane의 pre-Gold seal 상태를 보존해야 한다면 내부 field로 남기고,
최종 dossier에는 별도 Gold status를 붙인다.

## stale self-repair artifact

self-repair audit가 과거 snapshot이라면 다음 중 하나를 수행한다.

```text
A. final canonical state로 재생성
또는
B. snapshot_status=SUPERSEDED_PRE_FINAL
   superseded_by=<final artifact id>
   production_readiness_authority=false
```

최종 문서에서:

```text
score_valid=false
stage_final=false
```

와

```text
score_valid=true
stage_final=true
```

가 같은 현재 상태인 것처럼 공존하면 FAIL이다.

## Lifecycle artifact

```json
{
  "artifact_id": "...",
  "artifact_path": "...",
  "artifact_role": "CURRENT_AUTHORITY|HISTORICAL_SNAPSHOT|SUPERSEDED",
  "as_of_date": "...",
  "generated_at": "...",
  "commit_sha": "...",
  "supersedes": [],
  "superseded_by": null,
  "production_readiness_authority": true
}
```

## Hard acceptance

```text
current authority contradiction count = 0
stale snapshot masquerading current count = 0
pending status after Gold PASS count = 0
score/stage receipt mismatch count = 0
```

커밋:

```text
Phase 104 운영 문서 상태와 artifact 생명주기를 원자적으로 정리하다
```

---

# 10. Phase 105 — Current Cross-Archetype Canary Selection

C06 외 다음 아키타입을 반드시 검증한다.

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

## 종목명 하드코딩 금지

production source/query/scoring 코드에 symbol-specific branch를 만들지 않는다.

canary target 선택은 다음 pre-deep 정보만 사용한다.

```text
- current KRX eligibility
- current trigger evidence
- issuer/business profile
- current official/report/news/price lane availability
- archetype compatibility
```

final score나 Stage를 본 뒤 target을 선택하면 FAIL이다.

## Pre-deep SelectionReceipt

```json
{
  "selection_id": "...",
  "archetype_id": "...",
  "target_id": "...",
  "company_name": "...",
  "selection_mode": "NATURAL_TRIGGER_CANARY|FORCED_VALIDATION_CANARY",
  "selection_as_of_date": "...",
  "pre_deep_input_hash": "...",
  "trigger_event_ids": [],
  "available_source_families": [],
  "selection_rationale": "...",
  "final_score_visible_at_selection": false,
  "final_stage_visible_at_selection": false
}
```

자연 trigger가 약하더라도 current full-pipeline 일반화 검증을 위해
`FORCED_VALIDATION_CANARY`는 허용한다.

단, 이를 daily production candidate로 가장하면 안 된다.

## 선택 조건

각 아키타입에 대해:

```text
- active current KRX-listed issuer
- 현재 source fetch 가능
- 해당 business mechanism과 직접 관련
- deep run 전 target seal 생성
- expected score 없음
- expected Stage 없음
```

## Hard acceptance

```text
required archetype selected count = 5
post-score target selection count = 0
target-specific code branch count = 0
forced canary mislabeled natural count = 0
```

커밋:

```text
Phase 105 다섯 아키타입 current canary를 점수 비노출 상태로 봉인하다
```

---

# 11. Phase 106 — C08/C15/C17/C24/C28 Current Live Researcher Mode

각 selected target을 실제 current source로 실행한다.

## Provider

```text
provider_selected_explicitly = true
provider_route = COLLABORATION_CODEX_SUBAGENT
automatic_qwen_fallback = false
automatic_ollama_fallback = false
LLM total score authority = false
LLM Stage authority = false
```

Qwen/Ollama 실험 코드가 저장소에 남아 있어도,
이번 operational acceptance에서 call count는 0이어야 한다.

## 실행 계약

각 target:

```text
business-model research
source graph acquisition
full document fetch
structured financial/consensus/valuation
EvidenceFact + counterfact
7 component memo
Analyst/Skeptic/Calibration Judge
deterministic score
deterministic StageCourt
```

## Completion

```text
production_research_complete = true
component memo = 7/7
material gap = 0
score_valid = true
StageCourt = FINAL
provider error = 0
query count > 0
document count > 0
fact count > 0
counterfact count > 0
```

숫자형 검색 한도 도달은 completion이 아니다.
transport checkpoint는 resume하되,
semantic completion 전에는 final score를 열지 않는다.

## Independent post-run review

각 canary마다 별도 Codex reviewer 2개 이상이 다음을 검토한다.

```text
- material fact 누락
- counterfact 누락
- wrong subject/segment
- currentness
- source quality
- component 점수 과소/과대
- historical anchor 동형성
```

Reviewer는 expected score/Stage를 받지 않는다.

## Tracked receipt

각 current canary도 Phase 101과 동일한 compact receipt를 커밋한다.

## Hard acceptance

```text
current live canary count = 5
7/7 memo target count = 5
score_valid target count = 5
FINAL StageCourt target count = 5
provider error count = 0
qwen/ollama call count = 0
target-specific branch count = 0
score lineage missing count = 0
```

커밋:

```text
Phase 106 다섯 아키타입 current live 연구·점수·Stage를 완결하다
```

---

# 12. Phase 107 — 최신 실제 KRX Census Selective-Deep

이 phase는 synthetic fixture가 아니다.

실행 시점에 사용 가능한 최신 KRX universe와 최신 거래 snapshot을 사용한다.

## 날짜

```text
execution_date_kst
latest_available_trading_snapshot_date
source_available_at
```

를 별도로 기록한다.

미래 날짜를 추정하지 않는다.

## Universe

실제 provider로:

```text
raw universe
eligible universe
excluded universe
exclusion reason
duplicate/missing symbol
market
listing status
```

를 materialize한다.

## Trigger lanes

첫 trigger를 DART 하나로 제한하지 않는다.

최소 다음 lane을 실제로 연결하고 count를 기록한다.

```text
OFFICIAL_DISCLOSURE
ISSUER_IR_EARNINGS
TRUSTED_NEWS
REPORT_CONSENSUS_REVISION
PRICE_VOLUME_ANOMALY
RESEARCH_MEMORY_HINT
RISK_EVENT
```

lane 하나가 장애면 다른 lane을 계속 실행한다.

## Routing

```text
baseline/trigger detection:
deterministic + source-backed

research depth/source/query routing:
LLM Research Supervisor

score:
Deterministic Score Aggregator

Stage:
Deterministic StageCourt
```

## Selective depth

```text
L0: universe
L1: cheap baseline
L2: official light
L3: Researcher planning
L4: source acquisition
L5: full dossier
```

전 종목을 매일 L5로 돌리지 않는다.

그러나 `Census PASS`를 위해 다음은 필수다.

```text
natural researcher candidate count > 0
L3 count > 0
L4 count > 0
L5 completed count > 0
accepted scoring fact count > 0
score_valid row count > 0
FINAL StageCourt row count > 0
```

다음은 PASS 금지다.

```text
all Stage0
all Pending
all score null
all provider pending
L5 zero
accepted fact zero
score contribution zero
```

## Compact stage map

각 eligible symbol에 다음을 기록한다.

```json
{
  "symbol": "...",
  "company_name": "...",
  "market": "...",
  "assessment_as_of_date": "...",
  "latest_trading_snapshot_date": "...",
  "trigger_lane_ids": [],
  "maximum_depth": "L1|L2|L3|L4|L5",
  "research_status": "...",
  "current_score": null,
  "current_score_status": "COMPLETE|NO_CURRENT_COMPLETE_SCORE|RESEARCH_IN_PROGRESS",
  "last_effective_score": null,
  "canonical_stage": null,
  "last_effective_stage": null,
  "stage_status": "FINAL|NOT_OPEN|RESEARCH_IN_PROGRESS",
  "dossier_receipt_id": null,
  "pending_reason": null
}
```

기본 row에 억지 점수를 넣지 않는다.

하지만 deep-selected row는 실제 score/Stage까지 완결한다.

## Census 의미 분리

최종 라벨은:

```text
CURRENT_KRX_CENSUS_SELECTIVE_DEEP_OPERATIONAL_PASS
```

이다.

이 라벨을:

```text
전 종목 L5 full-thesis 완료
```

라고 설명하지 않는다.

정확한 의미:

```text
전 종목 baseline 상태판
+ 실제 다중 trigger
+ 실제 selective deep
+ 실제 일부 full score/Stage
+ 운영 재개 가능한 queue
```

## Hard acceptance

```text
real KRX universe source = true
synthetic target count = 0
eligible row coverage = 100%
missing/duplicate symbol = 0
natural trigger lane count >= 3
natural candidate count > 0
L5 completed count > 0
score_valid deep row count > 0
FINAL Stage deep row count > 0
provider-failed final score count = 0
snippet score count = 0
source-proxy current score count = 0
all-zero/all-pending false pass count = 0
```

커밋:

```text
Phase 107 최신 KRX Census에서 실제 후보·연구·점수·Stage를 연결하다
```

---

# 13. Phase 108 — One-Command Operational Acceptance

하나의 canonical command를 만든다.

예:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_v6_operational_acceptance_until_pass \
  --live-materialization-authorized true \
  --research-provider codex-collaboration \
  --verify-existing-c06-receipts true \
  --run-cross-archetype-canaries true \
  --run-current-krx-census true \
  --checkpoint-resume true \
  --export-tracked-receipts true \
  --run-clean-clone-verification true
```

## Command behavior

```text
1. current HEAD/config/provider fingerprint
2. C06 receipt verification
3. cross-archetype canary selection
4. current live canary runs
5. current KRX Census
6. tracked receipt export
7. reviewer gate
8. full tests
9. final cutover verdict
```

## Failure handling

실패하면 종료 보고만 하지 마라.

```text
failure class
→ exact root cause
→ code/prompt/provider/parser/source fix
→ focused test
→ clean rerun
→ receipt regeneration
→ reviewer rerun
```

을 수행한다.

외부 provider 하나가 실패하면 alternate public route를 시도한다.

모든 합법적 공개 route가 실제로 막힌 경우:

```text
EXTERNAL_BLOCKER_NOT_COMPLETE
```

로 기록한다.

이것은 Goal complete가 아니다.

## Checkpoint

process가 종료돼도:

```text
selection seal
source checkpoint
fact checkpoint
component memo checkpoint
judge checkpoint
receipt checkpoint
```

에서 재개한다.

fixed retry count는 final completion authority가 아니다.

커밋:

```text
Phase 108 운영 인수검사를 한 명령으로 재개·완료하게 만들다
```

---

# 14. Phase 109 — Independent Operational Reviewer Gate

기존 Reviewer A~J를 그대로 유지하고 모두 PASS여야 한다.

새 Operational Reviewer K~V를 추가한다.

## Reviewer K — Receipt Completeness

```text
actual scores/stages present
7 component values present
all score facts present
```

## Reviewer L — Receipt Referential Integrity

```text
fact/judge/anchor/source references
hashes
no orphan
```

## Reviewer M — Clean Clone Reproduction

```text
no output/cache/env
same score/stage
same receipt hash
```

## Reviewer N — Provider Honesty

```text
explicit Codex
actual provider calls
Qwen/Ollama 0
no automatic fallback
```

## Reviewer O — Artifact Lifecycle

```text
no stale/current contradiction
no pending-after-Gold wording
```

## Reviewer P — Cross-Archetype Generalization

```text
C08/C15/C17/C24/C28
7/7
score valid
final Stage
no target branch
```

## Reviewer Q — Current KRX Universe

```text
real universe
coverage
exclusions
no synthetic rows
```

## Reviewer R — Trigger and Routing

```text
multiple trigger lanes
LLM research routing
no DART-only trigger
```

## Reviewer S — Census Deep Path

```text
natural candidate
L3/L4/L5
accepted facts
score/stage
```

## Reviewer T — Score/Stage Atomicity

```text
component vector
total
StageCourt
same receipt
```

## Reviewer U — Security and Portability

```text
no secret
no absolute path identity
no local cache dependency
```

## Reviewer V — Final Operational Cutover

```text
all previous reviewers
full tests
origin/main
clean worktree
```

각 reviewer는 summary 문구를 믿지 않고 leaf를 직접 재계산한다.

```text
critical 1개
→ reviewer FAIL

reviewer 1개 FAIL
→ final FAIL
```

---

# 15. 필수 Known-Bad Tests

최소 다음을 추가한다.

```text
1. output/가 없는데 stale READY 문서만 있어 PASS
2. receipt total score 변조
3. component score 변조
4. canonical Stage 변조
5. scored support fact 삭제
6. scored counterfact 삭제
7. source URL 변조
8. quote hash 변조
9. judge decision 삭제
10. anchor ID 삭제
11. Gold fact를 Production receipt에 삽입
12. Gold query를 Production selection에 삽입
13. absolute /root path reviewer identity
14. Qwen 자동 fallback
15. Ollama 자동 fallback
16. provider call 0인데 live canary PASS
17. synthetic Census를 current KRX로 표시
18. all Stage0 Census PASS
19. all Pending Census PASS
20. L5 zero Census PASS
21. accepted fact zero Census PASS
22. provider failure final score
23. snippet score
24. source proxy current score
25. current target 선택을 final score 후 수행
26. forced canary를 natural candidate로 표시
27. target-specific symbol branch
28. expected score hardcoding
29. expected Stage hardcoding
30. 7개 component 중 하나 누락
31. component sum과 total 불일치
32. score receipt와 StageCourt input 불일치
33. event overlay가 canonical Stage 변경
34. stale self-repair snapshot이 current authority
35. Gold PASS 뒤 PENDING status가 current status
36. clean clone이 ~/.cache를 읽음
37. clean clone이 untracked collaboration journal을 읽음
38. full-test receipt tree hash stale
39. secret/env value receipt 노출
40. cross-archetype canary가 모두 C06 branch를 사용
41. no exact primitive → entire component zero
42. keyword-only support
43. counter ignored
44. duplicate fact point stacking
45. historical score copied to current
46. score change without fact/judge/anchor lineage
```

## Positive capability tests

```text
1. tracked receipt로 실제 component/total/Stage 재현
2. receipt-only clean clone PASS
3. official source support fact가 component 점수에 반영
4. counterfact가 net component를 낮춤
5. independent corroboration은 점수 중복 없이 confidence 증가
6. cross-archetype C08/C15/C17/C24/C28 각 1개 final
7. current KRX natural candidate가 L5와 FINAL Stage까지 진입
```

---

# 16. Self-Repair Until Operational PASS

고정 iteration 수로 완료 선언하지 않는다.

각 failure를 다음 schema로 기록한다.

```json
{
  "iteration_id": "...",
  "phase": "...",
  "target_or_scope": "...",
  "failure_class": "...",
  "root_cause": "...",
  "file_function_config": "...",
  "before_artifact_hash": "...",
  "patch_commit": "...",
  "focused_tests": [],
  "focused_test_status": "PASS",
  "clean_rerun_status": "PASS",
  "after_artifact_hash": "...",
  "remaining_blockers": []
}
```

Failure classes:

```text
RECEIPT_VALUE_MISSING
RECEIPT_LINEAGE_BROKEN
CLEAN_CLONE_DEPENDENCY
ABSOLUTE_PATH_IDENTITY
ARTIFACT_LIFECYCLE_CONTRADICTION
PROVIDER_ROUTE_MISMATCH
CROSS_ARCHETYPE_RESEARCH_INCOMPLETE
CURRENT_UNIVERSE_MATERIALIZATION_FAILED
TRIGGER_LANE_DISCONNECTED
NATURAL_CANDIDATE_ZERO
L5_RESEARCH_INCOMPLETE
SCORE_STAGE_ATOMICITY_FAILURE
FULL_TEST_STALE
SECRET_LEAK
TARGET_SPECIFIC_OVERFIT
```

각 failure class가 0이 될 때까지 수리한다.

---

# 17. Full Test와 Static Audit

최종 HEAD에서:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python -m compileall -q src tests
git diff --check
```

가능하면:

```bash
ruff check src tests
mypy 또는 pyright의 기존 project contract
```

도 실행한다.

## Test count

현재 baseline 6,637보다 감소하면:

```text
삭제된 테스트 목록
삭제 사유
대체 테스트
Reviewer 승인
```

이 없으면 FAIL이다.

skip/xfail로 acceptance를 우회하지 않는다.

## Static scans

```text
target-name-conditioned production branch
fixed expected score
fixed expected Stage
Gold path in production input
automatic Qwen/Ollama fallback
absolute reviewer path
secret literal
output-only readiness dependency
```

critical count 0.

---

# 18. Git Commit / Push 규칙

각 phase는 의미 있는 한글 커밋으로 분리한다.

예:

```text
Phase 101 삼성·하이닉스 실제 점수·Stage 검수 receipt를 공개하다
Phase 102 output 없이 receipt만으로 점수·Stage 재현을 완성하다
Phase 103 origin main clean clone 독립 재현을 증명하다
Phase 104 운영 문서 상태와 artifact 생명주기를 정리하다
Phase 105 다섯 아키타입 current canary를 비노출 상태로 봉인하다
Phase 106 다섯 아키타입 live 연구·점수·Stage를 완결하다
Phase 107 최신 KRX Census에서 실제 deep path를 연결하다
Phase 108 운영 인수검사를 한 명령으로 완성하다
Phase 109 독립 운영 reviewer와 최종 cutover를 확정하다
```

## 금지

```text
- report-only READY commit
- 테스트 실패 상태 push 후 완료 선언
- secret commit
- raw huge checkpoint commit
- 사용자 docs/core/goal*.md 변경 되돌리기
```

최종:

```text
HEAD == origin/main
worktree clean
```

을 확인한다.

최종 push 이후 origin/main clean clone을 다시 수행해야 한다.

---

# 19. GitHub에서 검수 가능한 필수 최종 문서

다음 문서 하나만 읽어도 현재 상태를 파악할 수 있어야 한다.

```text
docs/operational/e2r_v6_operational_cutover/operational_cutover_final.md
```

반드시 포함:

```text
1. exact final verdict
2. final HEAD
3. engine readiness
4. tracked receipt readiness
5. clean clone readiness
6. 삼성전자 7 component / total / Stage
7. SK하이닉스 7 component / total / Stage
8. C08 current canary target / total / Stage
9. C15 current canary target / total / Stage
10. C17 current canary target / total / Stage
11. C24 current canary target / total / Stage
12. C28 current canary target / total / Stage
13. current KRX universe counts
14. trigger lane counts
15. L0~L5 counts
16. natural candidate count
17. score_valid/FINAL Stage row count
18. provider routes and Qwen/Ollama calls
19. full-test count
20. Reviewer A~V
21. blockers
```

점수나 Stage를 숨기지 않는다.

---

# 20. 최종 Verdict 계층

기존 라벨:

```text
MEANINGFUL_E2R_RESEARCHER_PARITY_READY
```

는 engine/canary readiness다.

새 중간 라벨:

```text
E2R_V6_TRACKED_RECEIPT_REPRODUCIBLE_PASS
E2R_V6_CROSS_ARCHETYPE_LIVE_CANARY_PASS
E2R_V6_CURRENT_KRX_CENSUS_OPERATIONAL_PASS
```

최종 라벨:

```text
MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY
```

## 최종 라벨 Hard Gates

```text
기존 v5 Reviewer A~J PASS
새 Reviewer K~V PASS
critical sum = 0
blockers = []

삼성전자 actual score receipt present
SK하이닉스 actual score receipt present
두 target receipt-only recompute PASS
clean clone PASS

C08 current live final
C15 current live final
C17 current live final
C24 current live final
C28 current live final

real KRX universe materialized
real multi-lane triggers
natural candidate > 0
L5 completed > 0
score_valid rows > 0
FINAL Stage rows > 0

Qwen calls = 0
Ollama calls = 0
automatic non-Codex fallback = 0

full tests PASS
same evidence variance = 0
HEAD == origin/main
worktree clean
```

---

# 21. 절대 완료가 아닌 상태

다음은 Goal 완료가 아니다.

```text
- 삼성·하이닉스 score_valid=true만 있고 실제 점수 없음
- Stage final=true만 있고 실제 Stage 없음
- receipt가 output/ 없으면 깨짐
- clean clone이 로컬 cache를 읽음
- self-repair audit는 false, final doc은 true인 상태를 설명 없이 방치
- PENDING_POST_RUN_GOLD를 현재 completion 상태로 유지
- C06 두 종목만 통과
- cross-archetype canary가 fixture
- current Census가 synthetic target
- current Census L5가 0
- 모든 종목 Stage0/Unknown/Pending
- DART 단일 trigger lane
- Qwen/Ollama 자동 fallback
- report 문구만 READY
- 외부 blocker를 Goal complete로 표시
```

---

# 22. 최종 응답 형식

완료 후 다음 순서로 보고한다.

1. Final status
2. Final HEAD / origin / worktree
3. Phase commits
4. Existing v5 engine revalidation
5. Samsung actual component vector / total / Stage
6. Hynix actual component vector / total / Stage
7. Tracked receipt verification
8. Clean clone reproduction
9. Artifact lifecycle consistency
10. Cross-archetype canary selections
11. C08 actual result
12. C15 actual result
13. C17 actual result
14. C24 actual result
15. C28 actual result
16. Current KRX universe
17. Trigger lane distribution
18. L0~L5 distribution
19. Natural L5 completed rows and scores/Stages
20. Provider route / call counts / Qwen-Ollama counts
21. Full tests / positive / known-bad
22. Reviewer A~V
23. Self-repair iterations
24. Remaining blockers
25. Exact final verdict

---

# 23. 마지막 명령

이번 작업에서 또 scoring architecture를 갈아엎지 마라.

v5가 만든 연구원형 엔진을 그대로 보존하고,
그 결과를 **보이게 하고, 재현 가능하게 하고, 다른 아키타입과 실제 시장에서 작동시켜라.**

핵심 상태 전이는 다음이다.

```text
v5 canary READY
→ actual score/Stage tracked receipt
→ output 없는 clean clone 재계산
→ C08/C15/C17/C24/C28 current live final
→ real KRX Census natural candidate L5 final
→ independent operational reviewers
→ market cutover
```

실패하면 보호벽을 하나 더 추가하고 끝내지 마라.

```text
실패 leaf
→ 정확한 원인
→ 코드/프롬프트/source/parser 수정
→ clean rerun
→ receipt 재생성
→ clean clone 재검증
→ reviewer 재실행
```

까지 닫아라.

최종적으로 다음을 GitHub에서 독립 검수할 수 있을 때만 완료 선언하라.

```text
MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY
```
