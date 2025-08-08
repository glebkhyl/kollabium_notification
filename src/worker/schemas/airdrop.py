from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

__all__ = [
    "ClickInviterCtx",
    "ClickInviteeCtx",
    "NewRegCtx",
    "CondReadyCtx",
    "RewardCtx",
    "NewInviterCtx",
    "PlanChangedCtx",
]


class _UserMini(BaseModel):

    id: int = Field(..., alias="user_id")
    email: str
    plan: Optional[str] = None


class ClickInviterCtx(BaseModel):
    inviter_id: int
    inviter_email: str
    inviter_plan: Optional[str]
    ts: Optional[datetime] = None


class ClickInviteeCtx(BaseModel):
    invitee_id: int
    invitee_email: str
    invitee_plan: Optional[str]
    ts: Optional[datetime] = None


class NewRegCtx(BaseModel):
    inviter_id: int
    inviter_email: str
    inviter_plan: Optional[str]
    invitee_id: int
    invitee_email: str


class CondReadyCtx(NewRegCtx):
    """Условия AirDrop выполнены (тот же состав, что и NewReg)."""


class RewardCtx(NewRegCtx):
    reward: int
    sent_total: int
    remaining_total: int


class NewInviterCtx(BaseModel):
    invitee_id: int
    invitee_email: str
    invitee_plan: Optional[str]


class PlanChangedCtx(BaseModel):
    inviter_id: int
    inviter_email: str
    old_plan: str
    new_plan: str
    reward: int
