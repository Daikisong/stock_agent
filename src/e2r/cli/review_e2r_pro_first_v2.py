"""Run Pro-first V2 independent Reviewer A--H gates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.pro_first.independent_review_v2 import (
    run_independent_reviewers,
    write_independent_reviewer_receipt,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=1_200)
    args = parser.parse_args()
    receipt = run_independent_reviewers(
        Path(args.repo_root),
        timeout_seconds=args.timeout_seconds,
    )
    write_independent_reviewer_receipt(receipt, args.output)
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
    return 0 if receipt["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
