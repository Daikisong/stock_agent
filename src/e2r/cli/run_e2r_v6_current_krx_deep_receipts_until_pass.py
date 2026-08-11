"""Resume one natural current KRX L5 receipt through a semantic checkpoint."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Sequence

from e2r.production.v6_current_krx_deep_receipt_runner import (
    PHASE107_DEEP_RUN_PASS,
    PHASE107_DEEP_RUN_PENDING,
    V6CurrentKrxDeepReceiptRunner,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


DEFAULT_WORK_ROOT = Path("output/e2r_v6_operational_acceptance/phase107")


def _bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().casefold()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError("expected true or false")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--live-root", required=True)
    parser.add_argument("--work-root", default=str(DEFAULT_WORK_ROOT))
    parser.add_argument("--deep-receipt-root", required=True)
    parser.add_argument("--live-materialization-authorized", type=_bool, required=True)
    parser.add_argument("--checkpoint-resume", type=_bool, required=True)
    parser.add_argument(
        "--research-provider",
        choices=("codex-collaboration",),
        required=True,
    )
    parser.add_argument("--fact-documents-per-call", type=int, default=1)
    return parser


def _inside_repo(repo: Path, value: str, *, context: str) -> Path:
    raw = Path(value)
    supplied = Path(os.path.abspath(raw if raw.is_absolute() else repo / raw))
    if supplied != repo and repo not in supplied.parents:
        raise ValueError(f"{context} must remain inside the canonical repository")
    current = repo
    for part in supplied.relative_to(repo).parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f"{context} cannot traverse a symlink")
    path = supplied.resolve()
    if path != supplied:
        raise ValueError(f"{context} must preserve its canonical path identity")
    return path


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if not args.live_materialization_authorized or not args.checkpoint_resume:
        raise SystemExit("Phase107 requires live authorization and checkpoint resume")
    repo = Path(args.repo_root).resolve()
    if repo != canonical_repository_root() or not _repository_identity_is_trusted(repo):
        raise SystemExit("Phase107 must run from the clean trusted canonical repository")
    live = _inside_repo(repo, args.live_root, context="live root")
    expected_live = (repo / "output" / "live_materialization" / args.as_of_date).resolve()
    if live != expected_live or live.is_symlink() or not live.is_dir():
        raise SystemExit("Phase107 live root must be the canonical current materialization")
    work = _inside_repo(repo, args.work_root, context="work root")
    receipts = _inside_repo(repo, args.deep_receipt_root, context="deep receipt root")
    try:
        result = V6CurrentKrxDeepReceiptRunner().run_checkpoint(
            repo_root=repo,
            as_of_date=args.as_of_date,
            live_root=live,
            work_root=work,
            deep_receipt_root=receipts,
            live_materialization_authorized=True,
            checkpoint_resume=True,
            fact_documents_per_call=args.fact_documents_per_call,
        )
    except (OSError, RuntimeError, TypeError, ValueError, KeyError) as exc:
        print(
            json.dumps(
                {
                    "status": "E2R_V6_CURRENT_KRX_DEEP_RECEIPT_RUN_FAIL",
                    "error": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
                    "completion_based_on_fixed_retries": False,
                    "gold_call_count": 0,
                    "local_provider_call_count": 0,
                    "score_or_stage_authority": False,
                    "production_readiness_authority": False,
                },
                ensure_ascii=False,
                sort_keys=True,
                allow_nan=False,
            )
        )
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, allow_nan=False))
    if result.get("status") == PHASE107_DEEP_RUN_PASS:
        return 0
    if result.get("status") == PHASE107_DEEP_RUN_PENDING:
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
