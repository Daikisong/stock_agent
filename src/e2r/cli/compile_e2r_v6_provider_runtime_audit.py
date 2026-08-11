"""Compile the canonical v6 provider-runtime audit from sealed receipts."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets

from e2r.production.v6_provider_runtime_audit import (
    compile_provider_runtime_audit_from_cutover,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    FINAL_ROOT_RELATIVE,
    PROVIDER_RUNTIME_AUDIT_PASS,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--final-root", default=str(FINAL_ROOT_RELATIVE))
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
    final = (repo / args.final_root).resolve()
    canonical = (repo / FINAL_ROOT_RELATIVE).resolve()
    if final != canonical:
        raise SystemExit("provider audit requires the canonical cutover root")
    output = Path(args.output).resolve() if args.output else final / "provider_runtime_audit.json"
    if output != final / "provider_runtime_audit.json":
        raise SystemExit("provider audit output must be the canonical final leaf")
    result = compile_provider_runtime_audit_from_cutover(
        repo_root=repo,
        final_root=FINAL_ROOT_RELATIVE,
    )
    _write_json_atomic(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result.get("status") == PROVIDER_RUNTIME_AUDIT_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["_write_json_atomic", "main"]
