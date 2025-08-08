import os

from dotenv import load_dotenv

load_dotenv()

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")
AIR_DROP_LOG_BOT_TOKEN = os.getenv("AIR_DROP_LOG_BOT_TOKEN")
AIR_DROP_LOG_CHAT = int(os.getenv("AIR_DROP_LOG_CHAT", "-1002678250936"))


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
