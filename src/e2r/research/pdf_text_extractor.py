"""Optional PDF text extraction interface."""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
import logging
import math
from pathlib import Path
from statistics import median
from typing import Mapping
import unicodedata


_ALLOWED_TEXT_CONTROLS = frozenset("\n\r\t\f")
PDF_TEXT_EXTRACTION_SEMANTICS_VERSION = "e2r_pdf_text_extraction_v2"


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
    extraction_semantics_version: str | None = None


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
            import pdfplumber  # type: ignore
        except ImportError:
            pass
        else:
            available_extractors.append("pdfplumber")
            try:
                with pdfplumber.open(BytesIO(payload)) as pdf:
                    text = "\n".join(
                        _pdfplumber_page_text(page) for page in pdf.pages
                    )
                unreadable = extracted_text_unreadable_reason(text)
                if unreadable is None:
                    return PDFTextExtractionResult(
                        ok=True,
                        text=text,
                        extractor="pdfplumber",
                        extraction_semantics_version=(
                            PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
                        ),
                    )
                failures.append(f"pdfplumber_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pdfplumber_failed:{type(exc).__name__}:{exc}")

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
                        ok=True,
                        text=text,
                        extractor="pymupdf",
                        extraction_semantics_version=(
                            PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
                        ),
                    )
                failures.append(f"pymupdf_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pymupdf_failed:{type(exc).__name__}:{exc}")

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
                        ok=True,
                        text=text,
                        extractor="pypdf",
                        extraction_semantics_version=(
                            PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
                        ),
                    )
                failures.append(f"pypdf_unreadable:{unreadable}")
            except Exception as exc:  # pragma: no cover - optional library internals
                failures.append(f"pypdf_failed:{type(exc).__name__}:{exc}")

        if failures:
            return PDFTextExtractionResult(
                ok=False,
                reason=";".join(failures),
                extractor=available_extractors[-1],
                extraction_semantics_version=(
                    PDF_TEXT_EXTRACTION_SEMANTICS_VERSION
                ),
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


def _pdfplumber_page_text(page: object) -> str:
    """Preserve the visual row order and add a verified column-order variant.

    Corporate PDFs frequently place two or three narrative columns on one
    landscape page.  ``pdfplumber.extract_text`` then interleaves the columns
    row by row, so a visually contiguous paragraph is not a contiguous source
    quote.  Strong full-height whitespace gutters provide a generic layout
    signal.  Keep the default text for tables and append the column-order text
    only when those gutters are present; no source words are synthesized or
    discarded.
    """

    extractor = getattr(page, "extract_text", None)
    if not callable(extractor):
        return ""
    default_text = str(extractor() or "")
    column_bounds = _pdfplumber_column_bounds(page)
    if len(column_bounds) <= 1:
        return default_text
    crop = getattr(page, "crop", None)
    height = float(getattr(page, "height", 0.0) or 0.0)
    if not callable(crop) or height <= 0:
        return default_text
    column_parts: list[str] = []
    try:
        for left, right in column_bounds:
            column_page = crop((left, 0.0, right, height))
            column_extractor = getattr(column_page, "extract_text", None)
            if not callable(column_extractor):
                return default_text
            value = str(column_extractor() or "").strip()
            if value:
                column_parts.append(value)
    except Exception:  # pragma: no cover - optional pdfplumber internals
        return default_text
    column_text = "\n".join(column_parts)
    if (
        not column_text
        or column_text == default_text
        or extracted_text_unreadable_reason(column_text) is not None
    ):
        return default_text
    return f"{default_text}\n\f\n{column_text}"


def _pdfplumber_column_bounds(page: object) -> tuple[tuple[float, float], ...]:
    """Detect two/three-column narrative layouts from strong vertical gutters."""

    width = float(getattr(page, "width", 0.0) or 0.0)
    height = float(getattr(page, "height", 0.0) or 0.0)
    word_extractor = getattr(page, "extract_words", None)
    if width <= 0 or height <= 0 or not callable(word_extractor):
        return ()
    try:
        words = tuple(
            row
            for row in word_extractor(
                use_text_flow=False,
                keep_blank_chars=False,
            )
            if isinstance(row, Mapping)
        )
    except Exception:  # pragma: no cover - optional pdfplumber internals
        return ()
    body_words = tuple(
        row
        for row in words
        if float(row.get("bottom", 0.0) or 0.0) >= height * 0.05
        and float(row.get("top", height) or height) <= height * 0.95
        and float(row.get("x1", 0.0) or 0.0)
        > float(row.get("x0", 0.0) or 0.0)
    )
    if len(body_words) < 40:
        return ()
    step = max(2.0, width / 420.0)
    bin_count = max(1, math.ceil(width / step))
    occupancy = [0] * bin_count
    for word in body_words:
        left = max(0, min(bin_count - 1, int(float(word["x0"]) / step)))
        right = max(
            left,
            min(bin_count - 1, int(float(word["x1"]) / step)),
        )
        for index in range(left, right + 1):
            occupancy[index] += 1
    active = [value for value in occupancy if value > 0]
    if not active:
        return ()
    low_threshold = max(1.0, float(median(active)) * 0.08)
    text_left = min(float(row["x0"]) for row in body_words)
    text_right = max(float(row["x1"]) for row in body_words)
    text_span = text_right - text_left
    if text_span < width * 0.55:
        return ()
    minimum_gutter = max(12.0, width * 0.015)
    minimum_column = text_span * 0.18
    gutter_centers: list[float] = []
    index = 0
    while index < bin_count:
        if occupancy[index] > low_threshold:
            index += 1
            continue
        start = index
        while index < bin_count and occupancy[index] <= low_threshold:
            index += 1
        end = index
        gap_left = start * step
        gap_right = min(width, end * step)
        center = (gap_left + gap_right) / 2.0
        if (
            gap_right - gap_left >= minimum_gutter
            and center - text_left >= minimum_column
            and text_right - center >= minimum_column
        ):
            gutter_centers.append(center)
    if not gutter_centers:
        return ()
    boundaries = [max(0.0, text_left - step), *gutter_centers, min(width, text_right + step)]
    if any(
        right - left < minimum_column
        for left, right in zip(boundaries, boundaries[1:])
    ):
        return ()
    return tuple(zip(boundaries, boundaries[1:]))


def _path_exists(value: str) -> bool:
    try:
        return Path(value).exists()
    except OSError:
        return False


__all__ = [
    "PDF_TEXT_EXTRACTION_SEMANTICS_VERSION",
    "PDFTextExtractionResult",
    "PDFTextExtractor",
    "extracted_text_unreadable_reason",
]
