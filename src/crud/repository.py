from sqlalchemy import (
    Result,
    Select,
    Tuple,
    and_,
    asc,
    desc,
    func,
    or_,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.database import new_session
from crud.models import AirDropUsers, AlertText, User


class CRUDRepository:

    @classmethod
    async def get_air_drop_data(cls, user_id) -> AirDropUsers:
        async with new_session() as session:
            drop_query = await session.execute(
                select(AirDropUsers).where(AirDropUsers.user_id == user_id)
            )
            return drop_query.scalars().first()

    @classmethod
    async def get_user_with_apliner(cls, user_id):
        async with new_session() as session:
            user_query = await session.execute(
                select(User)
                .where(User.id == user_id)
                .options(joinedload(User.mentor))
            )
            return user_query.scalars().first()

    @classmethod
    async def get_user_data(cls, user_id):
        async with new_session() as session:
            user_query = await session.execute(
                select(User).where(User.id == user_id)
            )
            return user_query.scalars().first()

    @classmethod
    async def get_user_telegram_id(cls, user_id):
        async with new_session() as session:
            user_query = await session.execute(
                select(User.telegram_id).where(User.id == user_id)
            )
            return user_query.scalars().first()

    @classmethod
    async def get_alert_text(cls, alert_type, lang="ru"):
        async with new_session() as session:
            text_query = await session.execute(
                select(AlertText.text).where(
                    AlertText.type == alert_type,
                    AlertText.active == True,
                    AlertText.lang == lang,
                )
            )
            return text_query.scalars().first()
