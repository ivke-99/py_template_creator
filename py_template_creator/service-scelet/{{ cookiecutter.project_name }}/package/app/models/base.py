import logging
import datetime as dt
from package.app import settings
from sqlalchemy import create_engine, Identity, BigInteger, func
from sqlalchemy.schema import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    MappedAsDataclass,
    Mapped,
    mapped_column,
    scoped_session,
)


class CreatedMixin(MappedAsDataclass):
    created_at: Mapped[dt.datetime] = mapped_column(
        default=None, server_default=func.now(), kw_only=True
    )
    # updated_at: Mapped[dt.datetime] = mapped_column(
    #     default=None,
    #     server_default=func.now(),
    #     onupdate=func.now(),
    #     kw_only=True,
    # )


class IdMixin(MappedAsDataclass):
    id: Mapped[int] = mapped_column(
        BigInteger, Identity(always=True), init=False, primary_key=True
    )


class Base(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    """subclasses will be converted to dataclasses"""


logger = logging.getLogger(__name__)

DB_URL = "postgresql+psycopg://{}:{}@{}:{}/{}".format(
    settings.POSTGRES_USER,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOST,
    settings.POSTGRES_PORT,
    settings.POSTGRES_DB,
)
logger.info(f"Connecting with conn string {DB_URL}")


engine = create_engine(
    DB_URL,
    pool_pre_ping=True,
    pool_size=settings.MAX_THREADS,
    pool_recycle=3600,
    echo=False,
)
session_maker = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Session = scoped_session(session_maker)
