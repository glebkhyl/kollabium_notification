from decimal import Decimal

from core.utils import to_msk
from crud.repository import CRUDRepository
from sinks import REGISTRY
from texts.donats_logs_telegram import DonatsLogs


async def handle_new_donat_created(ctx: dict, profile: str) -> None:
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


async def handle_donat_payed(ctx: dict, profile: str) -> None:
    donation_data = await CRUDRepository.get_air_drop_donations(
        order_id=ctx.get("order_id")
    )
    user_data = await CRUDRepository.get_user_data(
        user_id=donation_data.user_id
    )
    time = to_msk(donation_data.created_at)
    data = {
        "donat_id": ctx.get("order_id"),
        "amount": donation_data.amount,
        "time": time,
        "user_name": user_data.username,
    }
    text = DonatsLogs.render("ADMIN_DONAT_PAYED", **data)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})


async def handle_payment_failed(ctx: dict, profile: str) -> None:
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
        "amount": donation_data.amount,
        "time": time,
        "user_name": user_data.username,
    }
    user_text_data = {"amount": donation_data.amount}
    text = DonatsLogs.render("ADMIN_PAYMENT_FAILED", **data)
    user_text = DonatsLogs.render("DONAT_PAID_USER", **user_text_data)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})
    await REGISTRY["logs.telegram"].send(
        {"text": user_text, "chat_id": user_data.telegram_id}
    )


async def tokens_airdrop_user(ctx: dict) -> None:
    job_data = await CRUDRepository.get_air_drop_job(id=ctx.get("job_id"))
    user_data = await CRUDRepository.get_user_data(user_id=job_data.user_id)
    kol_amount = Decimal(job_data.tokens) / Decimal(10**18)
    data = {"kol_amount": f"{kol_amount.normalize():f}"}
    text = DonatsLogs.render("TOKENS_AIRDROP_USER", **data)
    await REGISTRY["logs.telegram"].send(
        {"text": text, "chat_id": user_data.telegram_id}
    )
