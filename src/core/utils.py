import re
from datetime import datetime, timedelta


def format_telegram_message(template: str, **params) -> str:
    filled = template.format(**params)

    def _repl(match: re.Match) -> str:
        lng = len(match.group(0))
        return "\n\n" if lng == 3 else "\n"

    formatted = re.sub(r"[ \t]{2,3}", _repl, filled)
    return formatted.strip()


def to_msk(dt: datetime) -> datetime:
    if dt is None:
        return None
    return dt + timedelta(hours=3)
