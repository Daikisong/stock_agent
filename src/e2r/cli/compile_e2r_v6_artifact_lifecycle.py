"""Compile the tracked E2R v6 artifact-lifecycle audit atomically."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import secrets

from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    ARTIFACT_LIFECYCLE_PASS,
    CANONICAL_MANIFEST_NAME,
    FINAL_ROOT_RELATIVE,
    compile_artifact_lifecycle,
    load_artifact_lifecycle_manifest,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--final-root", default=str(FINAL_ROOT_RELATIVE))
    parser.add_argument("--output", required=True)
    return parser


def _path_or_parent_is_symlink(path: Path) -> bool:
    current = path
    while True:
        if current.is_symlink():
            return True
        if current == current.parent:
            return False
        current = current.parent


def _output_overlaps_inputs(
    output: Path,
    *,
    manifest_path: Path,
    repo_root: Path,
    artifact_paths: tuple[str, ...],
) -> bool:
    if _path_or_parent_is_symlink(output):
        return True
    try:
        output_resolved = output.resolve()
        if output_resolved == manifest_path.resolve():
            return True
    except OSError:
        return True
    for relative in artifact_paths:
        try:
            artifact = (repo_root / relative).resolve()
        except OSError:
            return True
        if output_resolved == artifact:
            return True
        if output.exists() and artifact.exists():
            try:
                if os.path.samefile(output, artifact):
                    return True
            except OSError:
                return True
    return False


def _write_json_atomic(path: Path, payload: object) -> None:
    """Write result-last with file and directory durability."""

    if path.is_symlink() or _path_or_parent_is_symlink(path.parent):
        raise ValueError("artifact lifecycle output path cannot use symlinks")
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
                raise ValueError("unsafe lifecycle output parent component")
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


def main() -> int:
    args = _parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    manifest_path = Path(args.manifest)
    canonical_manifest_path = repo_root / FINAL_ROOT_RELATIVE / CANONICAL_MANIFEST_NAME
    if (
        manifest_path.is_symlink()
        or manifest_path.resolve() != canonical_manifest_path.resolve()
    ):
        raise SystemExit("artifact lifecycle manifest must be the canonical tracked file")
    raw_output = Path(args.output)
    output = raw_output.resolve()
    manifest = load_artifact_lifecycle_manifest(manifest_path)
    artifact_paths = tuple(
        str(row.get("artifact_path") or "")
        for row in manifest.get("artifacts", ())
        if isinstance(row, dict)
    )
    if _output_overlaps_inputs(
        raw_output,
        manifest_path=manifest_path,
        repo_root=repo_root,
        artifact_paths=artifact_paths,
    ):
        raise SystemExit(
            "artifact lifecycle output cannot overwrite or alias an input"
        )
    result = compile_artifact_lifecycle(
        manifest,
        repo_root=repo_root,
        final_root=args.final_root,
        prospective_audit_path=output,
    )
    _write_json_atomic(output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == ARTIFACT_LIFECYCLE_PASS else 2


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["_output_overlaps_inputs", "_write_json_atomic", "main"]
