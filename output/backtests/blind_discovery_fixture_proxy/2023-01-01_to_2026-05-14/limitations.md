# Blind Discovery Limitations

- Historical search/report snapshots are point-in-time evidence; benchmark labels are not evidence.
- If snapshots are unavailable, the replay marks misses instead of pretending success.
- Benchmark labels are evaluation-only and are not used by E2R_STANDARD candidate generation.
- Stage 3-Green thresholds are not loosened for recall.
- fixture proxy mode was enabled explicitly; this is regression only, not blind discovery proof.
- fixture proxy mode; not proof of live discovery
