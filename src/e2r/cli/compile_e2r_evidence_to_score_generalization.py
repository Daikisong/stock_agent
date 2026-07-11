"""Compile C08/C15 and semantic-guard evidence-to-score canaries."""

from __future__ import annotations

import argparse
import json

from e2r.research_brain.scoring.generalization_canaries import compile_evidence_to_score_generalization_audit


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="docs/operational/e2r_evidence_to_score_generalization_audit.json")
    args = parser.parse_args(argv)
    result = compile_evidence_to_score_generalization_audit(output_path=args.output)
    print(json.dumps({"status":result["status"],"critical_count_sum":result["critical_count_sum"]},sort_keys=True))
    return 0 if result["critical_count_sum"] == 0 else 2


if __name__ == "__main__": raise SystemExit(main())
