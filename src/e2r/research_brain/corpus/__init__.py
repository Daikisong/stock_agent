"""Canonical historical research corpus ingestion."""

from e2r.research_brain.corpus.research_corpus_parser import (
    is_structured_row,
    parse_historical_research_artifact,
)
from e2r.research_brain.corpus.research_case_linker import (
    link_research_rows,
)

__all__ = [
    "is_structured_row",
    "link_research_rows",
    "parse_historical_research_artifact",
]
