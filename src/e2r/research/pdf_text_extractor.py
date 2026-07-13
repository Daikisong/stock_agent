"""Optional PDF text extraction interface."""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
import logging
import math
from pathlib import Path
from typing import Mapping
import unicodedata


_ALLOWED_TEXT_CONTROLS = frozenset("\n\r\t\f")


def extracted_text_unreadable_reason(text: str) -> str | None:
    """Return a stable reason when extracted text is not human-readable.

    PDF libraries can report a successful extraction even when a custom font
    maps most glyphs to C0 control characters.  Korean and other non-Latin
    scripts remain valid; only characters that cannot represent ordinary
    document text (or a large number of Unicode replacement markers) are
    rejected here.
    """

    if not text.strip():
        return "empty_extracted_text"
    length = len(text)
    minimum_bad_characters = max(8, math.ceil(length * 0.02))
    control_count = sum(
        unicodedata.category(character) == "Cc"
        and character not in _ALLOWED_TEXT_CONTROLS
        for character in text
    )
    if control_count >= minimum_bad_characters:
        return f"excessive_control_characters:{control_count}/{length}"
    replacement_count = text.count("\ufffd")
    if replacement_count >= minimum_bad_characters:
        return f"excessive_unicode_replacement_characters:{replacement_count}/{length}"
    return None


@dataclass(frozen=True)
class PDFTextExtractionResult:
    """PDF extraction result with capability errors represented as data."""

    ok: bool
    text: str | None = None
    reason: str | None = None
    extractor: str | None = None


@dataclass(frozen=True)
class PDFTextExtractor:
    """Extract text from PDFs or mapped local text fixtures."""

    fixture_text_by_path: Mapping[str, str | Path] | None = None

    def extract_text(self, file_path: str | Path) -> PDFTextExtractionResult:
        path = Path(file_path)
        mapped = self._fixture_text(str(path))
        if mapped is not None:
            return PDFTextExtractionResult(ok=True, text=mapped, extractor="fixture")
        if path.suffix.lower() == ".txt" and path.exists():
            return PDFTextExtractionResult(ok=True, text=path.read_text(encoding="utf-8"), extractor="txt")
        adjacent_text = path.with_suffix(".txt")
        if adjacent_text.exists():
            return PDFTextExtractionResult(ok=True, text=adjacent_text.read_text(encoding="utf-8"), extractor="adjacent_txt")
        if not path.exists():
            return PDFTextExtractionResult(ok=False, reason=f"file not found: {path}")
        return self.extract_text_from_bytes(path.read_bytes())

    def extract_text_from_bytes(self, payload: bytes) -> PDFTextExtractionResult:
        failures: list[str] = []
        available_extractors: list[str] = []
        try:
            import fitz  # type: ignore
        except ImportError:
            pass
        else:
            available_extractors.append("pymupdf")
            try:
                with fitz.open(stream=payload, filetype="pdf") as document:
                    text = "\n".join(page.get_text() for page in document)
                unreadable = extracted_text_unreadable_reason(text)
                if unreadable is None:
                    return PDFTextExtractionResult(
                        ok=True, text=text, extractor="pymupdf"
                    )
                failures.append(f"pymupdf_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pymupdf_failed:{type(exc).__name__}:{exc}")

        try:
            import pdfplumber  # type: ignore
        except ImportError:
            pass
        else:
            available_extractors.append("pdfplumber")
            try:
                with pdfplumber.open(BytesIO(payload)) as pdf:
                    text = "\n".join(page.extract_text() or "" for page in pdf.pages)
                unreadable = extracted_text_unreadable_reason(text)
                if unreadable is None:
                    return PDFTextExtractionResult(
                        ok=True, text=text, extractor="pdfplumber"
                    )
                failures.append(f"pdfplumber_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pdfplumber_failed:{type(exc).__name__}:{exc}")

        try:
            from pypdf import PdfReader  # type: ignore
        except ImportError:
            pass
        else:
            available_extractors.append("pypdf")
            try:
                logging.getLogger("pypdf").setLevel(logging.ERROR)
                reader = PdfReader(BytesIO(payload))
                text = "\n".join(page.extract_text() or "" for page in reader.pages)
                unreadable = extracted_text_unreadable_reason(text)
                if unreadable is None:
                    return PDFTextExtractionResult(
                        ok=True, text=text, extractor="pypdf"
                    )
                failures.append(f"pypdf_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pypdf_failed:{type(exc).__name__}:{exc}")

        if failures:
            return PDFTextExtractionResult(
                ok=False,
                reason=";".join(failures),
                extractor=available_extractors[-1],
            )
        return PDFTextExtractionResult(
            ok=False,
            reason=(
                "PDF extraction requires PyMuPDF, pdfplumber, pypdf, "
                "or a local .txt fixture"
            ),
        )

    def _fixture_text(self, key: str) -> str | None:
        if not self.fixture_text_by_path:
            return None
        if key not in self.fixture_text_by_path:
            return None
        value = self.fixture_text_by_path[key]
        if isinstance(value, Path) or (isinstance(value, str) and _path_exists(value)):
            return Path(value).read_text(encoding="utf-8")
        return str(value)


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


__all__ = [
    "PDFTextExtractionResult",
    "PDFTextExtractor",
    "extracted_text_unreadable_reason",
]
