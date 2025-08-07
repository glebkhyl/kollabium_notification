import html
import os

from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from icecream import ic

from core.config import AIR_DROP_LOG_BOT_TOKEN, AIR_DROP_LOG_CHAT
from sinks.base import Sink, register

ic(AIR_DROP_LOG_BOT_TOKEN)


@register
class TelegramSink(Sink):
    channel = "logs.telegram"

    def __init__(self):
        self.bot = Bot(
            AIR_DROP_LOG_BOT_TOKEN,
            default=DefaultBotProperties(parse_mode="HTML"),
        )
        self.chat = int(AIR_DROP_LOG_CHAT)

    async def send(self, payload: dict):
        await self.bot.send_message(self.chat, payload["text"])
