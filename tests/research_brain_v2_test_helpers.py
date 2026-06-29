import json
from pathlib import Path

from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix


def load_v2_cards():
    matrix = json.loads(Path("docs/operational/research_brain_v1_archetype_matrix.json").read_text(encoding="utf-8"))
    return build_memory_cards_from_v1_matrix(matrix)


def load_json(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))
