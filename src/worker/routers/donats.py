from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from uuid import uuid4

from faststream.nats import NatsMessage, NatsRouter
from icecream import ic

from core.nats_client import (
    publish_logs,
    publish_schedule,
    stream_logs,
    stream_sched,
    stream_user,
)
from worker.events import donats
from worker.metrics import logs_consume_failed_total, logs_consume_total

router = NatsRouter()


@router.subscriber("donats", queue="donats-workers", stream=stream_logs)
async def route_airdrop(event: dict):
    subject = "donats"
    kind = str(event.get("kind", ""))
    if event.get("channel") != "donats":
        return
    ic()
    try:
        if kind == "ADMIN_NEW_DONAT_CREATED":
            await donats.handle_new_donat_created(
                event.get("ctx") or {}, event.get("profile")
            )
        elif kind == "ADMIN_DONAT_PAYED":
            await donats.handle_donat_payed(
                event.get("ctx") or {}, event.get("profile")
            )
        # elif kind == "ADMIN_TOKENS_SENT":
        #     await airdrop.handle_new_reg(
        #         event.get("ctx") or {}, event.get("profile")
        #     )
        # elif kind == "ADMIN_PAYMENT_EXPIRED":
        #     await airdrop.handle_tokens_sent(
        #         event.get("ctx") or {}, event.get("profile")
        #     )
        else:
            return

        logs_consume_total.labels(subject=subject, kind=kind).inc()
    except Exception as e:
        logs_consume_failed_total.labels(
            subject=subject, kind=kind, error=type(e).__name__
        ).inc()
        raise
