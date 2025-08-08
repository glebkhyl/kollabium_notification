# worker/events/registry.py
from collections import defaultdict
from typing import Any, Awaitable, Callable

# handlers[channel][kind] -> coroutine
_HANDLERS: dict[
    str, dict[str, Callable[[dict[str, Any]], Awaitable[None]]]
] = defaultdict(dict)


def register(channel: str, kind: str):
    """Декоратор: @register("airdrop", "CLICK_INVITER")"""

    def decorator(fn: Callable[[dict[str, Any]], Awaitable[None]]):
        _HANDLERS[channel][kind] = fn
        return fn

    return decorator


async def dispatch(event: dict[str, Any]) -> None:
    """Вызвать нужный хендлер (если есть)."""
    channel = event.get("channel")
    kind = event.get("kind")
    if channel and kind:
        handler = _HANDLERS.get(channel, {}).get(kind)
        if handler:
            await handler(event["ctx"])
            return

    # сюда дошли ‒ подходящего хендлера нет
    from logging import getLogger

    getLogger(__name__).warning(
        "no handler for channel %s / kind %s", channel, kind
    )
