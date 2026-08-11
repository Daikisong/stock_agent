"""Compile the strict Phase-107 current KRX selective-deep cutover leaves."""

from __future__ import annotations

import argparse
import json
import os
import secrets
import stat
from pathlib import Path

from e2r.production.v6_current_krx_census import (
    CURRENT_KRX_CENSUS_PASS,
    compile_current_krx_census_cutover,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    _repository_identity_is_trusted,
    canonical_repository_root,
)


CUTOVER_RELATIVE_ROOT = Path("docs/operational/e2r_v6_operational_cutover")


def _parse_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"expected boolean, got {value!r}")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of-date", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--live-root", required=True)
    parser.add_argument("--deep-receipt-root", required=True)
    parser.add_argument("--check-only", type=_parse_bool, default=False)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo = Path(args.repo_root).resolve()
    canonical = canonical_repository_root()
    if repo != canonical:
        raise SystemExit("current KRX cutover must run from the canonical repository")
    if not args.check_only and not _repository_identity_is_trusted(repo):
        raise SystemExit("current KRX cutover publish requires a trusted clean repository")
    live_root = _inside_repo(repo, args.live_root, context="live root")
    receipt_root = _inside_repo(
        repo,
        args.deep_receipt_root,
        context="deep receipt root",
    )
    summary, stage_rows = compile_current_krx_census_cutover(
        assessment_as_of_date=args.as_of_date,
        live_root=live_root,
        deep_receipt_root=receipt_root,
    )
    output_paths: dict[str, str] = {}
    if summary["status"] == CURRENT_KRX_CENSUS_PASS and not args.check_only:
        cutover_root = repo / CUTOVER_RELATIVE_ROOT
        if not cutover_root.is_dir() or cutover_root.is_symlink():
            raise SystemExit("canonical cutover root must already exist as a real directory")
        map_path = cutover_root / "current_krx_stage_map_compact.jsonl"
        summary_path = cutover_root / "current_krx_census_summary.json"
        _write_bytes_atomic(
            map_path,
            "".join(
                json.dumps(row, ensure_ascii=False, sort_keys=True, allow_nan=False)
                + "\n"
                for row in stage_rows
            ).encode("utf-8"),
        )
        # The summary is the commit marker and is published last.  Its
        # ``stage_map_hash`` binds the already-fsynced JSONL rows.
        _write_bytes_atomic(
            summary_path,
            (
                json.dumps(
                    summary,
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                    allow_nan=False,
                )
                + "\n"
            ).encode("utf-8"),
        )
        output_paths = {
            "summary": str(summary_path),
            "stage_map": str(map_path),
        }
    print(
        json.dumps(
            {
                **summary,
                "output_paths": output_paths,
            },
            ensure_ascii=False,
            sort_keys=True,
            allow_nan=False,
        )
    )
    return 0 if summary["status"] == CURRENT_KRX_CENSUS_PASS else 2


def _inside_repo(repo: Path, value: str, *, context: str) -> Path:
    path = (repo / value).resolve() if not Path(value).is_absolute() else Path(value).resolve()
    if path != repo and repo not in path.parents:
        raise SystemExit(f"{context} must remain inside the repository")
    return path


def _write_bytes_atomic(path: Path, encoded: bytes) -> None:
    parent_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    directory_fd = os.open(path.parent, parent_flags)
    temporary_name = f".{path.name}.{secrets.token_hex(12)}.tmp"
    descriptor: int | None = None
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=directory_fd,
        )
        with os.fdopen(descriptor, "wb") as handle:
            descriptor = None
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(
            temporary_name,
            path.name,
            src_dir_fd=directory_fd,
            dst_dir_fd=directory_fd,
        )
        final_fd = os.open(
            path.name,
            os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=directory_fd,
        )
        try:
            metadata = os.fstat(final_fd)
            if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
                raise ValueError("atomic output is not a single-link regular file")
            chunks: list[bytes] = []
            while True:
                chunk = os.read(final_fd, 65536)
                if not chunk:
                    break
                chunks.append(chunk)
            if b"".join(chunks) != encoded:
                raise ValueError("atomic output verification mismatch")
        finally:
            os.close(final_fd)
        os.fsync(directory_fd)
    finally:
        if descriptor is not None:
            os.close(descriptor)
        try:
            os.unlink(temporary_name, dir_fd=directory_fd)
        except FileNotFoundError:
            pass
        os.close(directory_fd)


if __name__ == "__main__":
    raise SystemExit(main())
