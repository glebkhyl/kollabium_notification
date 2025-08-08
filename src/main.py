import json

from faststream import FastStream

from core.nats_client import broker
from worker.events.registry import dispatch
from worker.routers.airdrop import router as airdrop_router

# @broker.subscriber("logs.events", stream=stream, queue="log-workers")
# async def handle_log(event: dict):
#     inner = event.get("message") or {}
#     if isinstance(inner, str):  # пришло строкой → парсим
#         inner = json.loads(inner)
#     if isinstance(inner, dict):
#         inner.setdefault("channel", event.get("channel"))
#         await dispatch(inner)
#     else:
#         # ничего не получилось разобрать
#         await dispatch(event)


# @broker.subscriber("logs.events", stream=stream, queue="log-workers")
# async def handle_log(event: dict):
#     # event = {"channel": "...", "level": "...", "message": {...}}
#
#     inner = event.get("message") or {}  # достаём вложенный словарь
#     if isinstance(inner, str):  # если пришло как JSON-строка
#         import json
#
#         inner = json.loads(inner)
#
#     merged_event = {  # делаем то, что ждёт dispatch()
#         "channel": event.get("channel"),
#         "kind": inner.get("kind"),
#         "ctx": inner.get("ctx", {}),
#     }
#
#     await dispatch(merged_event)


fs = FastStream(broker)
broker.include_router(airdrop_router)
