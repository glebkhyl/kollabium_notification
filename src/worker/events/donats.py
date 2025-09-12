from faststream.nats import message
from icecream import ic

from core.template_loader import render
from core.utils import format_telegram_message, to_msk
from crud.repository import CRUDRepository
from sinks import REGISTRY
from texts.airdrop_logs import AirdropLogs
from texts.donats_logs_telegram import DonatsLogs


async def handle_new_donat_created(ctx: dict, profile: str) -> None:
    ic()
    donation_data = await CRUDRepository.get_air_drop_donations(
        order_id=ctx.get("order_id")
    )
    user_data = await CRUDRepository.get_user_data(
        user_id=donation_data.user_id
    )
    fio = f"{user_data.first_name} {user_data.last_name}"
    time = to_msk(donation_data.created_at)
    data = {
        "donat_id": ctx.get("order_id"),
        "fio": fio,
        "user_id": user_data.id,
        "email": user_data.email,
        "user_name": user_data.username,
        "amount": donation_data.amount,
        "time": time,
    }
    text = DonatsLogs.render("ADMIN_NEW_DONAT_CREATED", **data)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})
