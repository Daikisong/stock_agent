# 0618 TODO: 운영형 Stage 승격 병목 점검

## 목적

0612 패치로 삼성전자와 SK하이닉스는 실제 운영형 파이프라인에서 다음이 확인됐다.

- 가격 데이터가 들어온다.
- OpenDART 공식 재무 actual이 들어온다.
- post-score-gap 경고가 있어도 `visible_score`가 유지된다.
- Stage는 둘 다 `3-Yellow`로 산출된다.

0618 작업의 목적은 "왜 고득점인데 `3-Green`으로 승격되지 않는지"를 찾는 것이다.

## 중요 원칙

삼성전자와 SK하이닉스는 운영형 회귀 테스트 샘플일 뿐이다.

패치에서 다음은 금지한다.

- `symbol == "005930"` 조건
- `symbol == "000660"` 조건
- `company_name`에 `삼성전자`, `SK하이닉스`, `하이닉스`가 있으면 점수 보정
- HBM/반도체 케이스만 맞추기 위한 종목명 특화 예외
- 특정 과거 성공 종목을 기준으로 Green을 강제로 여는 로직

허용되는 패치는 다음뿐이다.

- 모든 종목에 적용되는 feature 추출 개선
- 모든 종목에 적용되는 LLM evidence expansion 개선
- 모든 종목에 적용되는 Green gate 진단 개선
- 모든 종목에 적용되는 disclosure/consensus/revision/actual 연결 개선
- 아키타입별 일반 규칙 개선

쉽게 말하면 삼성전자와 SK하이닉스는 체온계다. 체온계가 열을 보여줬다고 체온계 이름을 코드에 박으면 안 된다. 병의 원인, 즉 공통 로직 병목을 고쳐야 한다.

## 다음 작업 순서

1. 삼성전자 1종목 운영형 재실행
   - `as_of_date=2026-06-12` 또는 작업일 기준 최신 날짜로 실행한다.
   - `fixture_mode=False`, `live_enabled=True`
   - `targeted_smoke_only=True`
   - page fetch와 Codex theme route provider를 켠다.

2. Green gate autopsy 작성
   - `visible_score`
   - component score
   - Stage reason
   - failed Green gates
   - `stage_gate_diagnostics`
   - `theme_route_diagnostics`
   - `score_gap` warning
   - evidence family count

3. 삼성전자에서 막힌 항목을 일반화해서 분류
   - 데이터가 실제로 없는가?
   - API에는 있는데 connector가 못 가져오는가?
   - 검색에는 있는데 parser가 못 읽는가?
   - LLM이 찾아야 하는데 suggested query가 약한가?
   - feature에는 있는데 deterministic scorer/gate가 반영하지 않는가?
   - gate 조건이 너무 보수적인가?

4. SK하이닉스로 같은 검증 반복
   - 삼성전자에서 찾은 병목이 하이닉스에도 재현되는지 본다.
   - 두 종목 공통이면 일반 로직 병목 가능성이 높다.
   - 한 종목만 발생하면 종목 특화 패치가 아니라 source/parsing/evidence 차이를 먼저 본다.

5. 일반 fixture 테스트 추가
   - 삼성전자/하이닉스 이름이 없는 가짜 종목 fixture를 만든다.
   - 같은 evidence shape을 넣었을 때 동일한 개선이 작동해야 한다.
   - 운영형 샘플 테스트와 generic fixture 테스트가 둘 다 통과해야 패치 가능하다.

## 확인해야 할 주요 병목 후보

### 1. `consensus_revisions`

0612 v6 결과:

| 종목 | consensus | consensus revisions |
|---|---:|---:|
| 삼성전자 | 1 | 0 |
| SK하이닉스 | 3 | 1 |

삼성전자는 리포트와 컨센서스가 있는데 revision이 0이다. 다음을 확인한다.

- CompanyGuide recent report payload에 목표가/EPS 상향 정보가 있는데 누락됐는가?
- report parser가 `EPS_ACTION_TYP_NM`, `PRC_ACTION_TYP_NM`을 revision evidence로 연결하지 못했는가?
- consensus revision이 feature input까지 들어오지 못했는가?

### 2. `disclosures=0`

0612 v6 결과에서 두 종목 모두 feature input의 disclosures가 0이다.

확인할 것:

- OpenDART date-range disclosure는 수집됐는가?
- detail fetch는 됐는데 대상 종목 필터에서 빠졌는가?
- 공시 타입이 routine으로 분류되어 feature input에서 무시됐는가?
- lookback window가 너무 짧아 최신 공시만 보고 있는가?

주의: routine 공시를 억지로 Green 증거로 쓰면 안 된다. 다만 분기/사업보고서에서 actual 또는 segment/HBM 관련 문장이 구조화될 수 있는지는 확인한다.

### 3. score-gap LLM 지연

0612 v6에서 LLM 호출은 정상 작동했지만 시간이 길었다.

확인할 것:

- score-gap context가 너무 길어 provider가 느려지는가?
- 이미 확보한 evidence를 다시 LLM에 과도하게 보내는가?
- 같은 gap signature가 반복되는데 stop 조건이 늦는가?
- suggested query가 너무 많아 검색과 page fetch가 반복되는가?

목표는 검색을 임의로 줄이는 것이 아니다. 같은 정보를 더 압축해서 LLM이 덜 헤매게 만드는 것이다.

### 4. Green gate 조건

고득점인데 `3-Yellow`이면 Green gate 중 하나가 막힌 것이다.

확인할 것:

- revision gate
- structural visibility gate
- independent evidence family gate
- red-team risk gate
- price-only/theme-only guard
- contract quality/RPO/backlog gate

예를 들어 실제 재무 actual, 컨센서스, 리포트, 뉴스, 가격이 다 있는데도 Green이 계속 막히면 gate가 너무 보수적일 수 있다. 반대로 HBM 계약의 물량/기간/취소조건/RPO가 없으면 Yellow가 맞을 수 있다.

## 패치 승인 기준

패치 전후로 반드시 확인한다.

- 삼성전자 운영형 결과
- SK하이닉스 운영형 결과
- 삼성전자/하이닉스 이름이 없는 generic fixture 테스트
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- scoring/staging/red-team production code에 종목명 조건이 없는지 확인

종목명 조건 금지 확인 예:

```bash
rg -n '"005930"|"000660"|삼성전자|하이닉스' src/e2r tests
```

단, fixture, 테스트명, 문서, 운영형 출력 경로에는 종목명이 있을 수 있다. 금지 대상은 production scoring/staging/red-team/feature gate 로직의 종목명 조건이다.

## 산출물

0618 작업 산출물은 다음 형태로 남긴다.

- `docs/core/0618/samsung_green_gate_autopsy_YYYY-MM-DD.md`
- `docs/core/0618/semis_green_gate_generalization_plan_YYYY-MM-DD.md`
- 필요하면 `docs/core/0618/hynix_green_gate_autopsy_YYYY-MM-DD.md`

각 문서는 "삼전이라서"가 아니라 "이 evidence shape이면 어느 아키타입에서도 어떻게 처리해야 하는지"를 기준으로 작성한다.
