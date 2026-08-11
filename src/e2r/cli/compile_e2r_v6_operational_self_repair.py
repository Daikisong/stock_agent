"""Compile or verify the canonical E2R v6 operational self-repair audit."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets

from e2r.production.v6_operational_self_repair import (
    SELF_REPAIR_AUDIT_LEAF,
    SELF_REPAIR_PASS,
    compile_operational_self_repair_audit,
    validate_operational_self_repair_audit,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    FINAL_ROOT_RELATIVE,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--final-root", default=str(FINAL_ROOT_RELATIVE))
    parser.add_argument("--verify-only", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    repo = Path(args.repo_root).resolve()
    requested = Path(args.final_root)
    final = requested.resolve() if requested.is_absolute() else (repo / requested).resolve()
    canonical = (repo / FINAL_ROOT_RELATIVE).resolve()
    if final != canonical:
        raise SystemExit("operational self-repair audit requires canonical final root")
    result = compile_operational_self_repair_audit(
        repo_root=repo,
        final_root=final,
    )
    path = final / SELF_REPAIR_AUDIT_LEAF
    if args.verify_only:
        try:
            stored = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            stored = {}
        valid = validate_operational_self_repair_audit(stored, recomputed=result)
        print(json.dumps({"status": "PASS" if valid else "FAIL", "audit": result}, ensure_ascii=False, sort_keys=True))
        return 0 if valid else 2
    _write_json_atomic(path, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result.get("status") == SELF_REPAIR_PASS else 2


def _write_json_atomic(path: Path, payload: object) -> None:
    encoded = (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
    parent_fd = _open_directory(path.parent)
    temporary = f".{path.name}.{secrets.token_hex(16)}.tmp"
    descriptor = -1
    try:
        descriptor = os.open(
            temporary,
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
        os.replace(temporary, path.name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
    finally:
        if descriptor >= 0:
            os.close(descriptor)
        try:
            os.unlink(temporary, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        os.close(parent_fd)


def _open_directory(path: Path) -> int:
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


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["main"]
