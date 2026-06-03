# LLM Research Analyst Layer

The LLM layer is optional and disabled unless explicitly configured.

It helps read and explain evidence.
It does not replace deterministic scoring.

## Allowed Jobs

```text
query expansion
document extraction review
contradiction / Red Team hints
Korean Stage explanation
```

Example:

```text
Report text mentions "수주잔고 증가" but no contract duration.
LLM output:
  missing_information: ["contract_duration_months"]
  suggested_queries: ["회사명 단일판매 공급계약 계약기간"]
```

## Forbidden Jobs

The LLM must not:

```text
decide final Stage alone
override deterministic score
invent contract amount, duration, RPO, prepayment, EPS, or FCF
fill missing fields
produce buy/sell recommendation wording
```

## Output Schema

The LLM output includes:

```text
confidence
extracted_claims
missing_information
contradiction_flags
suggested_queries
evidence_ids_used
hallucination_risk
insufficient_evidence
stage_explanation_ko
```

If evidence is weak:

```text
insufficient_evidence = true
```

## Red Team Use

Contradiction flags can become Red Team findings.

Example:

```text
positive report says backlog is strong
news says contract was delayed
-> contradiction flag
-> Red Team finding candidate
```

The final Stage still comes from the deterministic StageClassifier.
