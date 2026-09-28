"""Fixed ChatGPT Pro research prompt contract with durable run markers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .ids import canonical_hash


@dataclass(frozen=True)
class RenderedProPrompt:
    text: str
    prompt_hash: str
    output_filename: str


class ProResearchPromptContract:
    def __init__(self, template_path: str | Path | None = None) -> None:
        default = Path(__file__).resolve().parents[3] / "configs" / "e2r_pro_research_prompt_v1.md"
        self.template_path = Path(template_path) if template_path else default
        self.template = self.template_path.read_text(encoding="utf-8")
        for marker in ("{{RUN_ID}}", "{{JOB_ID}}", "{{OUTPUT_FILENAME}}"):
            if marker not in self.template:
                raise ValueError(f"Pro prompt template is missing marker: {marker}")

    def render(
        self,
        *,
        job_id: str,
        run_id: str,
        symbol: str,
        as_of_date: str,
    ) -> RenderedProPrompt:
        output_filename = f"E2R_PRO_{job_id}_{symbol}_{as_of_date}.md"
        text = (
            self.template.replace("{{RUN_ID}}", run_id)
            .replace("{{JOB_ID}}", job_id)
            .replace("{{OUTPUT_FILENAME}}", output_filename)
        )
        if "{{" in text or "}}" in text:
            raise ValueError("unresolved placeholder remains in Pro prompt")
        return RenderedProPrompt(
            text=text,
            prompt_hash=canonical_hash({"prompt": text}),
            output_filename=output_filename,
        )


__all__ = ["ProResearchPromptContract", "RenderedProPrompt"]
