# 구조

```text
기존 KoreaCheapScanner
  → ProCandidateSelector
  → ResearchPacketV1
  → 로그인된 Chrome / ChatGPT Pro
  → ResearchDossierV1
  → 기존 EvidenceFact compiler·lifecycle
  → 기존 EvidenceGapAssessment
  → 7 component memo / 21 evidence-only Judge
  → 기존 deterministic scorer
  → 기존 AtomicStageCourtV2
  → publication
```

새 플랫폼이 담당하는 것은 durable orchestration, browser UI adapter, capture/import 경계다. 새 점수 엔진과 새 Stage 엔진은 없다.

`ProFirstJobStore`의 SQLite 장부가 기준 상태다. 파일이 보이기만 한다고 다음 단계로 넘지 않고, packet hash·prompt hash·approval nonce·capture receipt·dossier hash를 장부와 대조한다.

쉬운 예: 다운로드 폴더에 예전 `.md` 파일이 있어도 현재 job의 run marker와 새 attachment key가 맞지 않으면 capture하지 않는다. “파일이 하나 보였다”가 아니라 “이번 전송에서 새로 생긴 정확한 결과”를 확인한다.

세 golden 경로는 다음을 다룬다.

- C06: 실적 전환과 공급 가시성, corroboration cap을 구분한다.
- C17: 원재료 counterfact가 열려 있으면 낮은 점수를 확정하지 않고 Stage 0 pending으로 보존한다.
- C28: ARR/renewal 근거는 쓰되 제품 범위가 다른 fact의 component 승격을 막는다.
