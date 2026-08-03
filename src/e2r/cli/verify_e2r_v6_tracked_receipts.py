"""Verify E2R v6 tracked receipts without production output or caches."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from e2r.research_brain.researcher_mode.tracked_receipts import (
    VERIFICATION_PASS,
    verify_receipts,
)


def _bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError("expected true or false")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt-root", required=True)
    parser.add_argument("--offline", type=_bool, default=True)
    return parser


def main() -> int:
    args = _parser().parse_args()
    if not args.offline:
        raise SystemExit("v6 tracked receipt verification is offline-only")
    result = verify_receipts(Path(args.receipt_root))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == VERIFICATION_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
