from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from core.database import Base


class AlertText(Base):
    __tablename__ = "alerttexts"

    id = Column(BigInteger, primary_key=True)
    type = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    lang = Column(String)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(BigInteger, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), default=1)
    hashed_password: str = Column(String(length=1024), nullable=False)
    avatar = Column(Text)
    first_name = Column(String)
    last_name = Column(String)
    telegram_id = Column(BigInteger)
    telegram_login = Column(String)
    phone = Column(String)
    locale = Column(String)
    birthday = Column(String)
    sex = Column(String)
    city = Column(String)
    country = Column(String)
    site = Column(String)
    zodiac_sign = Column(String)
    psychotype = Column(String)
    family_status = Column(String)
    email_verified_at = Column(TIMESTAMP)
    banned = Column(Boolean, default=False)
    remember_token = Column(String, nullable=True)
    email_confirmation_code = Column(String(length=10))
    phone_confirmation_code = Column(String(length=10))
    apliner_user_id = Column(BigInteger)
    is_active = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    verify_code = Column(Integer)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)
    deleted_at = Column(TIMESTAMP)
    rating = Column(Float, default=0)
    reg_type = Column(String)
    ref_code = Column(String)
    skin = Column(String)
    melody = Column(String)
    sid = Column(String)
    last_online = Column(TIMESTAMP)
    in_dialog = Column(Boolean, default=False)
    connected_timestamp = Column(BigInteger, default=0)
    alerts_type = Column(Text)
    wings = Column(Text)
    about = Column(Text)
    saw_greeting = Column(Boolean, default=False)
    saw_airdrop = Column(Boolean, default=False)
    promo_points = Column(BigInteger, default=0)

    mentor = relationship(
        "User",
        uselist=False,
        foreign_keys=[id],
        primaryjoin="User.apliner_user_id == User.id",
        viewonly=True,
    )


class AirDropUsers(Base):
    __tablename__ = "air_drop_users"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), unique=True)
    partner_id = Column(BigInteger, ForeignKey("users.id"))
    bonus = Column(Integer, default=0)
    ref_link = Column(Boolean, default=False)
    email_confirmed = Column(Boolean, default=False)
    avatar = Column(Boolean, default=False)
    profile = Column(Boolean, default=False)
    telegram = Column(Boolean, default=False)
    first_post = Column(Boolean, default=False)
    first_like = Column(Boolean, default=False)
    complited = Column(Boolean, default=False)
    plan_name = Column(Text, default=None)
    active = Column(Boolean, default=False)
    old_user = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)

    user_info = relationship(
        "User",
        uselist=False,
        foreign_keys=[user_id],
        primaryjoin="AirDropUsers.user_id == User.id",
        viewonly=True,
    )

    partner_info = relationship(
        "User",
        uselist=False,
        foreign_keys=[partner_id],
        primaryjoin=partner_id == User.id,
        viewonly=True,
    )


class AirDropDonations(Base):
    __tablename__ = "air_drop_donations"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    order_id = Column(BigInteger, nullable=False)
    order_type = Column(String, nullable=False)
    amount = Column(Integer, default=0)
    currency = Column(String)
    payed = Column(Boolean, default=None, nullable=True)
    status = Column(String, default="NEW")
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, onupdate=datetime.utcnow)


class QueueStatus:
    QUEUED = "QUEUED"
    SENDING = "SENDING"
    SENT = "SENT"
    RETRYING = "RETRYING"
    FAILED = "FAILED"
    MANUAL_REQUIRED = "MANUAL_REQUIRED"
    IN_PROGRESS = "IN_PROGRESS"


class AirdropJob(Base):
    __tablename__ = "airdrop_jobs"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    tokens = Column(String(64), nullable=False)
    status = Column(String(24), default=QueueStatus.QUEUED, index=True)
    amount = Column(Integer, default=0, nullable=True)
    currency = Column(String, nullable=True)
    retries = Column(Integer, default=0)
    error = Column(Text, nullable=True)
    attempts = Column(Integer, nullable=False, default=0)
    correlation_id = Column(String(128), nullable=True, index=True)
    meta = Column(Text, nullable=True)
    not_before = Column(TIMESTAMP, nullable=True, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    sent_at = Column(TIMESTAMP, nullable=True)
    started_at = Column(TIMESTAMP, nullable=True)
    finished_at = Column(TIMESTAMP, nullable=True)
