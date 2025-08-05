from core.nats_client import app, broker, stream


async def publish(kind: str, ctx: dict, channel: str = "logs.telegram"):
    await broker.publish({"kind": kind, "ctx": ctx}, channel, stream="logs")
