import asyncio

from core.models import Event
from sinks import REGISTRY

queues: dict[str, asyncio.Queue] = {
    name: asyncio.Queue(maxsize=1000) for name in REGISTRY
}


async def fanout(event: Event):
    for chan in event.notify:
        if chan in queues:
            await queues[chan].put(event)
