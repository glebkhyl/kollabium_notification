from dataclasses import dataclass


@dataclass(slots=True)
class Event:
    kind: str
    payload: dict
