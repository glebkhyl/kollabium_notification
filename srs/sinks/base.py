from abc import ABC, abstractmethod


class Sink(ABC):
    channel: str

    @abstractmethod
    async def send(self, payload: dict): ...


REGISTRY: dict[str, Sink] = {}


def register(cls):
    REGISTRY[cls.channel] = cls()
    return cls
