import asyncio
import logging

from core.nats_client import app, broker, stream
from core.router import dispatch
from sinks import REGISTRY

logging.basicConfig(level=logging.INFO)

for channel in REGISTRY.keys():

    @broker.subscriber(channel, stream=stream)
    async def _(event: dict):
        await dispatch(event)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)
