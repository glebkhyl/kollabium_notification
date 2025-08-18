from faststream.nats import message
from icecream import ic

from core.template_loader import render
from core.utils import format_telegram_message
from crud.repository import CRUDRepository
from sinks import REGISTRY
from texts.airdrop_logs import AirdropLogs
from worker.schemas.airdrop import ClickInviterCtx

__all__ = ["handle_click_inviter"]


async def handle_click_inviter(ctx: dict, profile: str) -> None:
    text = AirdropLogs.render("CLICK_INVITER", **ctx)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})


async def handle_new_reg(ctx: dict, profile: str) -> None:
    text = AirdropLogs.render("NEW_REG", **ctx)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})


async def telegram_air_drop_all_done(ctx: dict) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_all_done"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    if telegram_id:
        text = format_telegram_message(template=message, tokens=ctx["amount"])
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_changed_to_inviter(ctx: dict) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_changed_to_inviter"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    if telegram_id:
        text = format_telegram_message(template=message)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_start(ctx: dict) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_start"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    if telegram_id:
        text = format_telegram_message(template=message)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_invitee_start_program(ctx: str) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_invitee_start_program"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    slave_data = await CRUDRepository.get_user_data(user_id=ctx["slave"])
    name = (
        slave_data.first_name if slave_data.first_name else slave_data.username
    )
    if telegram_id:
        text = format_telegram_message(template=message, name=name)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_invitee_complite_program(ctx: str) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_invitee_complite_program"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    slave_data = await CRUDRepository.get_user_data(user_id=ctx["slave"])
    name = (
        slave_data.first_name if slave_data.first_name else slave_data.username
    )
    if telegram_id:
        data = {"name": name, "amount": ctx["amount"]}
        text = format_telegram_message(template=message, **data)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_invitee_need_buy_plan(ctx: str) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_invitee_need_buy_plan"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    slave_data = await CRUDRepository.get_user_data(user_id=ctx["slave"])

    name = (
        slave_data.first_name if slave_data.first_name else slave_data.username
    )
    if telegram_id:
        text = format_telegram_message(template=message, name=name)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_invitee_lose12_hours(ctx: str) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_invitee_lose12_hours"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    slave_data = await CRUDRepository.get_user_data(user_id=ctx["slave"])
    air_drop_data = await CRUDRepository.get_air_drop_data(
        user_id=ctx["slave"]
    )
    name = (
        slave_data.first_name if slave_data.first_name else slave_data.username
    )
    if telegram_id and air_drop_data.complited is not True:
        text = format_telegram_message(template=message, name=name)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )


async def telegram_air_drop_can_be_inviter(ctx: str) -> None:
    message = await CRUDRepository.get_alert_text(
        alert_type="telegram_air_drop_can_be_inviter"
    )
    telegram_id = await CRUDRepository.get_user_telegram_id(
        user_id=ctx["user_id"]
    )
    if telegram_id:
        text = format_telegram_message(template=message)
        await REGISTRY["logs.telegram"].send(
            {"text": text, "chat_id": telegram_id}
        )
