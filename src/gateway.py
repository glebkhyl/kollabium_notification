import asyncio
import json
import os

from core.models import Event
from core.router import fanout, queues
from faststream import FastStream, Logger
from faststream.nats import JStream, NatsBroker
from icecream import ic
from sinks import REGISTRY

STREAM = "logs_stream"
SUBJECT = "logs.events"

broker = NatsBroker(os.getenv("NATS_URL", "nats://nats:4222"))
app = FastStream(broker)
stream = JStream(name=STREAM)


@broker.subscriber(SUBJECT, stream=stream, durable="router")
async def route(msg: str, logger: Logger):
    event = Event.model_validate_json(msg)
    await fanout(event)


@app.on_startup
async def run_sinks():
    for name, sink in REGISTRY.items():
        asyncio.create_task(sink_worker(name, sink))


async def sink_worker(name: str, sink):
    q = queues[name]
    while True:
        event = await q.get()
        try:
            await sink.send(event)
        except Exception as e:
            ic(f"[{name}] error: {e}")
