from typing import Any, Awaitable, Callable

_HANDLERS: dict[str, Callable[[dict[str, Any]], Awaitable[None]]] = {}


def register(channel: str):
    def decorator(fn: Callable[[dict[str, Any]], Awaitable[None]]):
        _HANDLERS[channel] = fn
        return fn

    return decorator


async def dispatch(event: dict[str, Any]) -> None:

    channel: str = event.get("channel") or "logs"
    handler = _HANDLERS.get(channel)
    if handler:
        await handler(event)
    else:
        from logging import getLogger

        getLogger(__name__).warning("no handler for channel %s", channel)
