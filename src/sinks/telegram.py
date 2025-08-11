from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from icecream import ic
from loguru import logger

from core.profiles import PROFILES
from sinks.base import Sink, register

# from core.db import get_chat_by_user_id


@register
class TelegramSink(Sink):
    channel = "logs.telegram"

    async def send(self, payload: dict):

        text = payload["text"]
        if "profile" in payload:
            prof = PROFILES.get(payload["profile"])
            if not prof:
                logger.warning("Unknown TG profile: {}", payload["profile"])
                return
            bot = Bot(
                str(prof.token),
                default=DefaultBotProperties(parse_mode="HTML"),
            )

            await bot.send_message(prof.chat, text)
            return
        if "chat_id" in payload:
            if not payload["chat_id"]:
                logger.warning("User {} has no chat-id", payload["user_id"])
                return
            bot = Bot(
                PROFILES["users"].token,
                default=DefaultBotProperties(parse_mode="HTML"),
            )
            await bot.send_message(payload["chat_id"], text)
            return
        logger.warning("Bad telegram payload: {}", payload)
