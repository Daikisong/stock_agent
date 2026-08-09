"""Compile E2R v6 readiness from committed tracked receipts only."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets

from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    compile_tracked_readiness,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt-root", required=True)
    parser.add_argument("--output")
    return parser


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
    )
    parent_fd = _open_or_create_directory_no_symlinks(path.parent)
    temporary_name = f".{path.name}.{secrets.token_hex(16)}.tmp"
    descriptor = -1
    try:
        descriptor = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            descriptor = -1
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
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


def _open_or_create_directory_no_symlinks(path: Path) -> int:
    """Open/create a directory through pinned dirfds without following links."""

    absolute = path.absolute()
    descriptor = os.open(absolute.anchor, os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            if part in {"", ".", ".."}:
                raise ValueError("unsafe readiness output parent component")
            try:
                next_descriptor = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            except FileNotFoundError:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=descriptor)
                except FileExistsError:
                    pass
                next_descriptor = os.open(
                    part,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                    dir_fd=descriptor,
                )
            os.close(descriptor)
            descriptor = next_descriptor
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def _output_overlaps_receipts(output: Path, receipt_root: Path) -> bool:
    if output == receipt_root or receipt_root in output.parents:
        return True
    if output.is_symlink():
        return True
    if output.exists():
        for path in receipt_root.rglob("*"):
            if path.is_file() and not path.is_symlink():
                try:
                    if os.path.samefile(output, path):
                        return True
                except OSError:
                    return True
    return False


def main() -> int:
    args = _parser().parse_args()
    receipt_root = Path(args.receipt_root).resolve()
    if args.output:
        output = Path(args.output).resolve()
        if _output_overlaps_receipts(output, receipt_root):
            raise SystemExit("readiness output cannot overwrite a receipt input")
    result = compile_tracked_readiness(receipt_root)
    if args.output:
        # Write the exact path that was checked above.  Re-resolving the
        # caller-supplied spelling after validation would reopen a symlink race.
        _write_json_atomic(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == TRACKED_READINESS_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())
