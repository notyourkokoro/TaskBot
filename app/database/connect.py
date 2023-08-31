from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.utils.config import config

engine = create_async_engine(
    config.database_info.database_url,
    echo=False
)

async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)
