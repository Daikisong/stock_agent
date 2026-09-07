"""Cross-platform durability helpers for Pro-first local artifacts."""

from __future__ import annotations

import os
from pathlib import Path


def fsync_directory(path: str | Path) -> None:
    """Flush a directory entry where the operating system supports it.

    POSIX permits opening and fsyncing a directory after ``os.replace``.
    Windows does not expose that operation through ``os.open``; the file itself
    is still flushed before replacement, so the directory step is a documented
    no-op there instead of making the browser worker crash after a good write.
    """

    if os.name == "nt":
        return
    descriptor = os.open(Path(path), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


__all__ = ["fsync_directory"]
