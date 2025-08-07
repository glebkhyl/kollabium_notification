import os

from dotenv import load_dotenv

load_dotenv()

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")
AIR_DROP_LOG_BOT_TOKEN = os.getenv("AIR_DROP_LOG_BOT_TOKEN")
AIR_DROP_LOG_CHAT = int(os.getenv("AIR_DROP_LOG_CHAT", "-1002678250936"))
