from faststream import FastStream

from core.nats_client import broker, stream
from core.router import dispatch


@broker.subscriber(
    "logs.events",
    stream=stream,
    durable="log-worker",
    queue="log-workers",  # добавили для масштабирования
)
async def handle_log(event: dict):
    print("131")
    await dispatch(event)


app = FastStream(broker)  # <- ASGI-приложение
