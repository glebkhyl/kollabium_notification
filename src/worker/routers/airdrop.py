import json

from faststream.nats import NatsRouter
from icecream import ic

from worker.events import airdrop

router = NatsRouter()


@router.subscriber("logs.events", queue="airdrop-workers")
async def route_airdrop(event: dict):
    print(event)
    if event.get("channel") != "airdrop":
        return

    kind = event.get("kind")
    if kind == "CLICK_INVITER":
        await airdrop.handle_click_inviter(event["ctx"], event["profile"])
