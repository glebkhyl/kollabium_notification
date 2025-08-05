from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

import yaml
from jinja2 import BaseLoader, Environment, select_autoescape

_ROOT = Path(__file__).resolve().parents[1]
_TPL_PATH = _ROOT / "templates" / "telegram.yaml"

_env = Environment(
    loader=BaseLoader(),
    autoescape=select_autoescape(disabled=True),
    trim_blocks=True,
    lstrip_blocks=True,
)


@lru_cache(maxsize=1)
def _load_templates() -> dict[str, str]:
    with _TPL_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def render(kind: str, ctx: Mapping[str, Any]) -> str:
    tpl = _load_templates().get(kind)
    if tpl is None:
        raise ValueError(f"text '{kind}' not found")
    return _env.from_string(tpl).render(**ctx).strip()
