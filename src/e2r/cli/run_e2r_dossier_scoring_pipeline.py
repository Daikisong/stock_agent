"""Run organic claim-to-impact-to-component-to-StageCourt dossier scoring."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.dossier import run_dossier_scoring_pipeline
from e2r.research_brain.scoring import CodexEvidenceImpactProvider


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dossier-root", required=True)
    parser.add_argument("--target-id", required=True)
    parser.add_argument("--company-name", required=True)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--canonical-archetype", required=True)
    parser.add_argument("--max-claims", type=int)
    parser.add_argument("--reuse-proposals", action="store_true")
    parser.add_argument("--retry-failed-only", action="store_true")
    parser.add_argument("--retry-claim-id", action="append", default=[])
    args = parser.parse_args(argv)
    result = run_dossier_scoring_pipeline(
        dossier_root=args.dossier_root,
        target_id=args.target_id,
        company_name=args.company_name,
        as_of_date=args.as_of_date,
        archetype_id=args.canonical_archetype,
        impact_provider=CodexEvidenceImpactProvider.default(
            working_directory=Path.cwd()
        ),
        max_claims=args.max_claims,
        reuse_proposals=args.reuse_proposals,
        retry_failed_only=args.retry_failed_only,
        retry_claim_ids=args.retry_claim_id,
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["status"] == "ORGANIC_DOSSIER_FULL_SCORE_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
