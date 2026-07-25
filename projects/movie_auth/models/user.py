from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True
    )

    name: Mapped[str] = mapped_column(
    String(100)
    )

    email: Mapped[str] = mapped_column(
    String(200),
    unique=True
    )

    password: Mapped[str] = mapped_column(
    String(255)
    )