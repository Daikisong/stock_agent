"""Optional PDF text extraction interface."""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Mapping


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
        try:
            import fitz  # type: ignore

            document = fitz.open(stream=payload, filetype="pdf")
            text = "\n".join(page.get_text() for page in document)
            return PDFTextExtractionResult(ok=True, text=text, extractor="pymupdf")
        except ImportError:
            pass
        except Exception as exc:  # pragma: no cover - depends on optional library internals
            return PDFTextExtractionResult(ok=False, reason=f"PyMuPDF extraction failed: {exc}", extractor="pymupdf")

        try:
            import pdfplumber  # type: ignore

            with pdfplumber.open(BytesIO(payload)) as pdf:
                text = "\n".join(page.extract_text() or "" for page in pdf.pages)
            return PDFTextExtractionResult(ok=True, text=text, extractor="pdfplumber")
        except ImportError:
            return PDFTextExtractionResult(
                ok=False,
                reason="PDF extraction requires PyMuPDF or pdfplumber, or a local .txt fixture",
            )
        except Exception as exc:  # pragma: no cover - depends on optional library internals
            return PDFTextExtractionResult(ok=False, reason=f"pdfplumber extraction failed: {exc}", extractor="pdfplumber")

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


__all__ = ["PDFTextExtractionResult", "PDFTextExtractor"]
