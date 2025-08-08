# src/worker/airdrop_logs.py
class AirdropLogs:

    CLICK_INVITER = (
        '🚀 <b>Нажал кнопку "Участвовать"</b> 🚀\n\n'
        "↘️ <b>Пригласитель:</b> "
        "ID {inviter_id} | {inviter_email} | {inviter_plan}\n"
        "↖️ <b>Приглашённый:</b> "
        "ID {invitee_id} | {invitee_email} | {invitee_plan}"
    )

    NEW_REG = (
        "🤝 <b>Новая регистрация</b> 🤝\n\n"
        "↘️ <b>Пригласитель:</b> ID{inviter_id} | {inviter_email} | {inviter_plan}\n"
        "↖️ <b>Приглашённый:</b> ID{invitee_id} | {invitee_email}"
    )

    # INFO: добивить остальные
    @staticmethod
    def render(kind: str, **ctx) -> str:
        tpl = getattr(AirdropLogs, kind, None)
        if tpl is None:
            raise ValueError(f"Шаблон “{kind}” не найден")
        return tpl.format(**ctx).strip()
