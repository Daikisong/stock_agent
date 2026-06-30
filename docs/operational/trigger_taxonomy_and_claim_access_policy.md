# Trigger Taxonomy and Claim Access Policy

- Official Positive Trigger: accepted_claim_required
- Official Risk Trigger: accepted_claim_required
- Financial/Revision Trigger: accepted_claim_required
- Market Anomaly Trigger: investigation_only_never_score
- Information Trigger: accepted_claim_required
- Census Assessment Trigger: accepted_claim_required

## Claim Access

- trigger can open investigation
- only accepted claim can open score
- market anomaly cannot become score evidence
- headline/snippet cannot score without full source/date/quote/target validation
- source_proxy memory cannot score
- old risk cannot score without current OPEN lifecycle
- missing evidence is UNKNOWN, not ABSENT
