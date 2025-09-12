import os
from typing import Any, Dict, Optional

from faststream.nats import JStream, NatsBroker

from worker.metrics import logs_publish_failed_total, logs_publish_total

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")

broker = NatsBroker(NATS_URL)

# ВАЖНО: имена стримов совпадают с тем, что реально создано в NATS (/jsz показывает: logs, USER, SCHEDULE)
stream_logs = JStream(name="logs", subjects=["logs.*"])
stream_user = JStream(name="USER", subjects=["user.*"])
stream_sched = JStream(name="SCHEDULE", subjects=["schedule.*"])


async def publish_logs(
    msg: Dict[str, Any],
    *,
    headers: Optional[Dict[str, str]] = None,
) -> None:

    subject = "logs.events"
    try:
        await broker.publish(
            msg,
            subject=subject,
            stream="logs",
            headers=headers or {},
        )
        logs_publish_total.labels(
            subject=subject,
            channel=str(msg.get("channel", "")),
            kind=str(msg.get("kind", "")),
        ).inc()
    except Exception as e:
        logs_publish_failed_total.labels(
            subject=subject,
            error=type(e).__name__,
        ).inc()
        raise


async def publish_schedule(
    msg: Dict[str, Any],
    *,
    headers: Optional[Dict[str, str]] = None,
) -> None:

    subject = "schedule.airdrop"
    try:
        await broker.publish(
            msg,
            subject=subject,
            stream="SCHEDULE",
            headers=headers or {},
        )
        logs_publish_total.labels(
            subject=subject,
            channel=str(msg.get("channel", "")),
            kind=str(msg.get("kind", "")),
        ).inc()
    except Exception as e:
        logs_publish_failed_total.labels(
            subject=subject,
            error=type(e).__name__,
        ).inc()
        raise
