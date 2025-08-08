from icecream import ic

from core.template_loader import render
from sinks import REGISTRY
from texts.airdrop_logs import AirdropLogs
from worker.schemas.airdrop import ClickInviterCtx

__all__ = ["handle_click_inviter"]


async def handle_click_inviter(ctx: dict, profile: str):
    text = AirdropLogs.render("CLICK_INVITER", **ctx)
    await REGISTRY["logs.telegram"].send({"text": text, "profile": profile})
