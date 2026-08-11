"""Resume the sealed exact-five Phase-106 canaries through atomic cutover."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.v6_canary_selection import (
    FORCED_SELECTION,
    ISSUER_PROFILE_MANIFEST_NAME,
    load_current_issuer_business_profile_manifest,
    load_sealed_cross_archetype_canary_selection,
)
from e2r.production.v6_current_live_canary_runner import (
    PHASE106_RUN_PASS,
    PHASE106_RUN_PENDING,
    V6CurrentLiveCanaryRunner,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    FINAL_ROOT_RELATIVE,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


SELECTION_NAME = "cross_archetype_canary_selection.json"
DEFAULT_WORK_ROOT = Path("output/e2r_v6_operational_acceptance/phase106")


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
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--live-materialization-authorized", type=_bool, required=True)
    parser.add_argument("--checkpoint-resume", type=_bool, required=True)
    parser.add_argument(
        "--research-provider",
        choices=("codex-collaboration",),
        required=True,
    )
    parser.add_argument("--fact-documents-per-call", type=int, default=1)
    parser.add_argument("--work-root", default=str(DEFAULT_WORK_ROOT))
    return parser


def _unvalidated_selection_header(path: Path) -> Mapping[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("canonical Phase105 selection is unavailable")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("canonical Phase105 selection is invalid") from exc
    if not isinstance(payload, Mapping):
        raise ValueError("canonical Phase105 selection must be an object")
    return payload


def _load_inputs(
    *, repo_root: Path, selection_path: Path
) -> tuple[Mapping[str, Any], Mapping[str, Any] | None]:
    expected = (repo_root / FINAL_ROOT_RELATIVE / SELECTION_NAME).resolve()
    if selection_path.resolve() != expected:
        raise ValueError("Phase106 selection must come from the canonical cutover")
    header = _unvalidated_selection_header(selection_path)
    rows = tuple(
        row for row in header.get("selections") or () if isinstance(row, Mapping)
    )
    forced = any(row.get("selection_mode") == FORCED_SELECTION for row in rows)
    profile: Mapping[str, Any] | None = None
    if forced:
        as_of_date = str(header.get("selection_as_of_date") or "")
        profile = load_current_issuer_business_profile_manifest(
            selection_path.parent / ISSUER_PROFILE_MANIFEST_NAME,
            selection_as_of_date=as_of_date,
        )
    selection = load_sealed_cross_archetype_canary_selection(
        selection_path,
        issuer_business_profile_manifest=profile,
    )
    return selection, profile


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if not args.live_materialization_authorized or not args.checkpoint_resume:
        raise SystemExit(
            "Phase106 requires live materialization authorization and checkpoint resume"
        )
    repo = Path(args.repo_root).resolve()
    if repo != canonical_repository_root() or not _repository_identity_is_trusted(repo):
        raise SystemExit("Phase106 must run from the clean trusted canonical repository")
    cutover = repo / FINAL_ROOT_RELATIVE
    work = Path(args.work_root)
    if not work.is_absolute():
        work = repo / work
    selection, profile = _load_inputs(
        repo_root=repo,
        selection_path=cutover / SELECTION_NAME,
    )
    try:
        result = V6CurrentLiveCanaryRunner().run_checkpoint(
            repo_root=repo,
            selection=selection,
            issuer_business_profile_manifest=profile,
            work_root=work,
            cutover_root=cutover,
            live_materialization_authorized=True,
            checkpoint_resume=True,
            fact_documents_per_call=args.fact_documents_per_call,
        )
    except (OSError, RuntimeError, TypeError, ValueError) as exc:
        print(
            json.dumps(
                {
                    "status": "E2R_V6_CURRENT_LIVE_CANARY_RUN_FAIL",
                    "error": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
                    "completion_based_on_fixed_retries": False,
                    "gold_call_count": 0,
                    "local_provider_call_count": 0,
                },
                ensure_ascii=False,
                sort_keys=True,
                allow_nan=False,
            )
        )
        return 2
    print(
        json.dumps(
            result,
            ensure_ascii=False,
            sort_keys=True,
            allow_nan=False,
        )
    )
    if result.get("status") == PHASE106_RUN_PASS:
        return 0
    if result.get("status") == PHASE106_RUN_PENDING:
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
