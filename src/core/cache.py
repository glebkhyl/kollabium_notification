from functools import lru_cache


@lru_cache(maxsize=10_000)
async def get_chat_cached(user_id: int) -> int | None:
    ...
    # return await get_chat_by_user_id(user_id)
