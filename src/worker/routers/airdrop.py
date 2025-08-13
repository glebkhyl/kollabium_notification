from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from uuid import uuid4

from faststream.nats import NatsMessage, NatsRouter
from icecream import ic

from core.nats_client import publish_logs, publish_schedule
from worker.events import airdrop

router = NatsRouter()

_MAX_CHUNK_SEC = 6 * 60 * 60
SCHEDULE_SUBJECT_AIRDROP = "schedule.airdrop"

HANDLERS = {
    "telegram_air_drop_start": airdrop.telegram_air_drop_start,
    "telegram_air_drop_12_left": airdrop.telegram_air_drop_all_done,  # INFO: need
    "telegram_air_drop_all_done": airdrop.telegram_air_drop_all_done,
    "telegram_air_drop_can_be_inviter": airdrop.telegram_air_drop_can_be_inviter,
    "telegram_air_drop_changed_to_inviter": airdrop.telegram_air_drop_changed_to_inviter,
    "telegram_air_drop_invitee_start_program": airdrop.telegram_air_drop_invitee_start_program,
    "telegram_air_drop_invitee_lose12_hours": airdrop.telegram_air_drop_invitee_lose12_hours,
    "telegram_air_drop_invitee_complite_program": airdrop.telegram_air_drop_invitee_complite_program,
    "telegram_air_drop_invitee_need_buy_plan": airdrop.telegram_air_drop_invitee_need_buy_plan,
    "telegram_air_drop_invitee_to_be_inviter": airdrop.telegram_air_drop_all_done,  # INFO: need
}


@router.subscriber("logs.events", queue="airdrop-workers")
async def route_airdrop(event: dict):
    if event.get("channel") != "airdrop":
        return
    if event.get("kind") == "CLICK_INVITER":
        await airdrop.handle_click_inviter(
            event.get("ctx") or {}, event.get("profile")
        )


@router.subscriber("user.events", queue="airdrop-users")
async def route_airdrop_user(event: dict):
    if event.get("channel") != "telegram_airdrop_user":
        return
    handler = HANDLERS.get(event.get("kind"))
    if handler:
        await handler(event.get("ctx") or {})
    else:
        import logging

        logging.getLogger(__name__).warning(
            "airdrop: unhandled kind=%s", event.get("kind")
        )


@router.subscriber("schedule.airdrop", queue="airdrop-scheduler")
async def airdrop_scheduler(event: dict, msg: NatsMessage):
    kind = event.get("kind")
    deliver_at = _parse_deliver_at(event.get("deliver_at"))
    if not kind or not deliver_at:
        await msg.ack()
        return
    now = datetime.now(timezone.utc)
    if now < deliver_at:
        delay = (deliver_at - now).total_seconds()
        delay = max(1.0, min(delay, _MAX_CHUNK_SEC))
        await msg.nack(delay=delay)
        return

    payload = {
        "channel": "airdrop",
        "kind": kind,
        "profile": event.get("profile"),
        "ctx": event.get("ctx") or {},
    }
    msg_id = event.get("id") or str(uuid4())
    await publish_logs(payload, headers={"Nats-Msg-Id": msg_id})
    await msg.ack()


def _parse_deliver_at(value: Any) -> Optional[datetime]:
    if isinstance(value, datetime):
        return (
            value.astimezone(timezone.utc)
            if value.tzinfo
            else value.replace(tzinfo=timezone.utc)
        )
    if isinstance(value, (int, float)):
        ts = float(value)
        if ts > 1e12:
            ts /= 1000.0
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    if isinstance(value, str):
        s = value.strip()
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(s)
            return (
                dt.astimezone(timezone.utc)
                if dt.tzinfo
                else dt.replace(tzinfo=timezone.utc)
            )
        except Exception:
            try:
                ts = float(s)
                if ts > 1e12:
                    ts /= 1000.0
                return datetime.fromtimestamp(ts, tz=timezone.utc)
            except Exception:
                return None
    return None


async def schedule_airdrop_after(
    kind: str,
    *,
    hours: float,
    ctx: dict,
    profile: Optional[str] = None,
    id: Optional[str] = None,
) -> None:
    deliver_at = datetime.now(timezone.utc) + timedelta(hours=hours)
    await publish_schedule(
        {
            "id": id or str(uuid4()),
            "kind": kind,
            "profile": profile,
            "ctx": ctx,
            "deliver_at": deliver_at.isoformat(),
        }
    )


async def schedule_airdrop_in_12h(
    kind: str,
    *,
    ctx: dict,
    profile: Optional[str] = None,
    id: Optional[str] = None,
) -> None:
    await schedule_airdrop_after(
        kind, hours=12, ctx=ctx, profile=profile, id=id
    )
