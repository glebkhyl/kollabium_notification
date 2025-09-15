class DonatsLogs:

    ADMIN_NEW_DONAT_CREATED = (
        "💸 Новый донат\n"
        "🧾 ID: #{donat_id}  \n"
        "🔰 Пользователь: {fio}\n"
        "🔰 ID: {user_id} | {email}\n"
        "🔰 @{user_name}\n"
        "💰 Сумма: {amount} ₽\n"
        "🕓 Время: {time} (MSK)"
    )

    ADMIN_DONAT_PAYED = (
        "✅ Донат оплачен | {type}\n"
        "🧾 ID: #{donat_id}  \n\n"
        "🔰 Пользователь: {fio}\n"
        "🔰 ID: {user_id} | {email}\n"
        "🔰 Telegram: @{user_name}\n\n"
        "💰 Сумма: {amount} ₽\n"
        "💎 KOLLABIUM: {kol_amount}"
        "📅 Дата оплаты: {time}\n"
    )

    # ADMIN_TOKENS_SENT = (
    #     "🪙 Токены начислены\n"
    #     "🧾 ID: #{donat_id}  \n"
    #     "🔰 Пользователь: {fio}\n"
    #     "🔰 ID: {user_id} | {email}\n"
    #     "🔰 @{user_name}\n"
    #     "🔰 Курс: 1 KOL = {rate} ₽\n"
    #     "💰 Донат: {amount} ₽\n"
    #     "💎 KOLLABIUM: {kol_amount} KOL\n"
    #     "👛 Кошелёк: {wallet}\n"
    #     "📅 Дата: {time}"
    # )

    ADMIN_TOKENS_SENT = (
        "🪙 Токены отправлены\n"
        "🧾 ID задачи: #{donat_id}  \n\n"
        "🔰 Пользователь: {fio}\n"
        "🔰 ID: {user_id} | {email}\n"
        "🔰 Telegram: @{user_name}\n\n"
        "🔰 Курс: 1 KOL = {rate} ₽\n\n"
        "💰 Донат: {amount} ₽\n"
        "💎 KOLLABIUM: {kol_amount} KOL\n"
        "📅 Дата: {time}"
    )

    ADMIN_PAYMENT_FAILED = (
        "⏳ Донат получил статус FAIL\n"
        "🧾 ID: #{donat_id}  \n"
        "🔰 Пользователь: {fio}\n"
        "🔰 {user_id} | {email}\n"
        "🔰 @{user_name}\n"
        "💰 Сумма: {amount} ₽\n"
        "📅 {time} (MSK)"
    )

    ADMIN_PAYMENT_EXPIRED = (
        "⏳ Время оплаты истекло\n"
        "🧾 ID: #{donat_id}  \n"
        "🔰 Пользователь: {fio}\n"
        "🔰 {user_id} | {email}\n"
        "🔰 @{user_name}\n"
        "💰 Сумма: {amount} ₽\n"
        "📌 Статус: Неуспешная оплата — сессия завершена\n"
        "📅 {time} (MSK)"
    )

    DONAT_PAID_USER = (
        "✅ Донат оплачен\n\n"
        "✅ Спасибо! Ваш донат принят.\n\n"
        "💰 Сумма: {amount} ₽   \n\n"
        "💜 Благодарим вас за поддержку KollabiuM."
    )

    TOKENS_AIRDROP_USER = (
        "🪂 Токены начислены (AirDrop выполнен)\n\n"
        "🎉 Вы получили токены KOLLABIUM по AirDrop!\n\n"
        "🪙 Сумма: {kol_amount} KOL   \n\n"
        "🔥 Спасибо за вашу активность!"
    )

    @staticmethod
    def render(kind: str, **ctx) -> str:
        tpl = getattr(DonatsLogs, kind, None)
        if tpl is None:
            raise ValueError(f"Шаблон “{kind}” не найден")
        return tpl.format(**ctx).strip()
