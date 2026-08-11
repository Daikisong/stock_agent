"""Compile the canonical E2R v6 production static-audit leaf."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets

from e2r.production.v6_production_static_audit import (
    PRODUCTION_STATIC_AUDIT_LEAF,
    PRODUCTION_STATIC_AUDIT_PASS,
    compile_production_static_audit,
)


_FINAL_ROOT = Path("docs/operational/e2r_v6_operational_cutover")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--final-root", default=str(_FINAL_ROOT))
    parser.add_argument("--output")
    return parser


def _open_existing_directory_no_symlinks(path: Path) -> int:
    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            next_descriptor = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
                dir_fd=descriptor,
            )
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _write_json_atomic(path: Path, payload: object) -> None:
    encoded = (
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")
    parent_fd = _open_existing_directory_no_symlinks(path.parent)
    temporary_name = f".{path.name}.{secrets.token_hex(16)}.tmp"
    descriptor = -1
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
            0o600,
            dir_fd=parent_fd,
        )
        offset = 0
        while offset < len(encoded):
            offset += os.write(descriptor, encoded[offset:])
        os.fsync(descriptor)
        os.close(descriptor)
        descriptor = -1
        os.replace(
            temporary_name,
            path.name,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        os.fsync(parent_fd)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            os.unlink(temporary_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        os.close(parent_fd)


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo = Path(args.repo_root).resolve()
    requested_final = Path(args.final_root)
    final = (
        requested_final.resolve()
        if requested_final.is_absolute()
        else (repo / requested_final).resolve()
    )
    canonical_final = (repo / _FINAL_ROOT).resolve()
    if final != canonical_final:
        raise SystemExit("production static audit requires the canonical cutover root")
    # An explicit path is a check-only copy (for example RUNNER_TEMP in CI).
    # Phase108 omits --output and therefore always materializes the canonical
    # lifecycle leaf.
    output = Path(args.output).resolve() if args.output else final / PRODUCTION_STATIC_AUDIT_LEAF
    if output.name != PRODUCTION_STATIC_AUDIT_LEAF:
        raise SystemExit("production static audit output filename is noncanonical")
    result = compile_production_static_audit(repo_root=repo)
    _write_json_atomic(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False))
    return 0 if result.get("status") == PRODUCTION_STATIC_AUDIT_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["_write_json_atomic", "main"]
