import os

from faststream.nats import JStream, NatsBroker

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")

broker = NatsBroker(NATS_URL)

stream = JStream(
    name="logs",
    subjects=["logs.*"],
)


async def publish_logs(msg: dict, *, headers: dict | None = None):
    await broker.publish(msg, subject="logs.events", headers=headers)


async def publish_schedule(msg: dict):
    await broker.publish(msg, subject="schedule.airdrop")
