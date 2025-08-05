import os

NATS_URL = os.getenv("NATS_URL", "nats://127.0.0.1:4222")
TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT = int(os.getenv("TG_CHAT", 0))
