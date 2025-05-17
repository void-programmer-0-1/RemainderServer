from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio.session import AsyncSession

from settings.settings import app_settings
from typing import AsyncGenerator


async_engine = create_async_engine(
    app_settings.database_url,
    connect_args={"check_same_thread": False},
    echo=True
)

async_session_local = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_local() as session:
        yield session


async def close_db():
    await async_engine.dispose()

    