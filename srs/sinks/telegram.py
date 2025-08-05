import html
import os

from aiogram import Bot
from core.config import TG_CHAT, TG_TOKEN
from sinks.base import Sink, register


@register
class TelegramSink(Sink):
    channel = "logs.telegram"

    def __init__(self):
        self.bot = Bot(TG_TOKEN, parse_mode="HTML")
        self.chat = TG_CHAT

    async def send(self, payload: dict):
        await self.bot.send_message(self.chat, payload["text"])
