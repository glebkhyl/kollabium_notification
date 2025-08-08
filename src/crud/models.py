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
