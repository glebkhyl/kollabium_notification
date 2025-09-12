import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class TgProfile:
    token: str
    chat: int


PROFILES: dict[str, TgProfile] = {
    "airdrop_logs": TgProfile(
        token=os.getenv(
            "AIR_DROP_BOT_TOKEN",
            "6675627103:AAFa5LR3RydEV0Az5tFvwdPbnzf2nE5FPl4",
        ),
        chat=int(os.getenv("AIR_DROP_CHAT_ID", "-1002678250936")),
    ),
    "donats_admin_logs": TgProfile(
        token=os.getenv(
            "USERS_BOT_TOKEN",
            "6094800971:AAF1_u23PEoSurmX-MnKi3mwkGvunY2ZhZ4",
        ),
        chat=int(os.getenv("DONAT_CHAT_ID", "-1003046720444")),
    ),
    "bbs": TgProfile(
        token=os.getenv("BBS_BOT_TOKEN"),
        chat=int(os.getenv("BBS_CHAT_ID", "-1001234567890")),
    ),
    "devops": TgProfile(
        token=os.getenv("DEVOPS_BOT_TOKEN"),
        chat=int(os.getenv("DEVOPS_CHAT_ID", "-1009876543210")),
    ),
    "payments": TgProfile(
        token=os.getenv("PAY_BOT_TOKEN"),
        chat=int(os.getenv("PAY_CHAT_ID", "-1001112223334")),
    ),
    "users": TgProfile(
        token=os.getenv("USERS_BOT_TOKEN"),
        chat=None,
    ),
}
