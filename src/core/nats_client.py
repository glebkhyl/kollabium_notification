# src/core/nats_client.py  – в воркере FastStream
import os

from faststream.nats import JStream, NatsBroker

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")

broker = NatsBroker(NATS_URL)

stream = JStream(
    name="logs",
    subjects=["logs.*"],
)
