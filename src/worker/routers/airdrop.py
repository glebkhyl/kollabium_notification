import json

from faststream.nats import NatsRouter
from icecream import ic

from worker.events import airdrop

router = NatsRouter()


HANDLERS = {
    "telegram_air_drop_start": airdrop.telegram_air_drop_start,
    "telegram_air_drop_12_left": airdrop.telegram_air_drop_all_done,
    "telegram_air_drop_all_done": airdrop.telegram_air_drop_all_done,
    "telegram_air_drop_can_be_inviter": airdrop.telegram_air_drop_all_done,
    "telegram_air_drop_changed_to_inviter": airdrop.telegram_air_drop_changed_to_inviter,
    "telegram_air_drop_invitee_start_program": airdrop.telegram_air_drop_invitee_start_program,
    "telegram_air_drop_invitee_lose12_hours": airdrop.telegram_air_drop_all_done,
    "telegram_air_drop_invitee_complite_program": airdrop.telegram_air_drop_invitee_complite_program,
    "telegram_air_drop_invitee_need_buy_plan": airdrop.telegram_air_drop_invitee_need_buy_plan,
    "telegram_air_drop_invitee_to_be_inviter": airdrop.telegram_air_drop_all_done,
}


@router.subscriber("logs.events", queue="airdrop-workers")
async def route_airdrop(event: dict):
    if event.get("channel") != "airdrop":
        return

    kind = event.get("kind")
    if kind == "CLICK_INVITER":
        await airdrop.handle_click_inviter(event["ctx"], event["profile"])


@router.subscriber("user.events", queue="airdrop-users")
async def route_airdrop(event: dict):
    if event.get("channel") != "telegram_airdrop_user":
        return

    handler = HANDLERS.get(event.get("kind"))
    if handler:
        await handler(event["ctx"])
    else:
        from logging import getLogger

        getLogger(__name__).warning(
            "unhandled kind=%s for airdrop", event.get("kind")
        )
