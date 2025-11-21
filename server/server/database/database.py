from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, text
import asyncpg
Base = declarative_base()

class APIKeys(Base):
    __tablename__ = 'api_keys'

    api_key_id = Column(Integer, primary_key=True)
    api_key = Column(String, unique=True, nullable=False)
    api_user_name = Column(String)
    access = Column(Integer)


class Files(Base):
    __tablename__ = 'files'

    file_id = Column(Integer, primary_key=True)
    file_name = Column(String, unique=True, nullable=False)
    file_creator = Column(String, ForeignKey("api_keys.api_key"))
    create_date = Column(String)
    file_size = Column(String)


async def init_db():
    DB_URL = "postgresql+asyncpg://postgres:1234@192.168.3.3:5432/storage"
    engine = create_async_engine(DB_URL, echo=True, pool_timeout=30)
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT version()"))
        version = result.scalar()
        print(f"PostgreSQL version: {version}")

    # Закрываем подключение
    await engine.dispose()

    print("Таблицы созданы успешно!")
    await engine.dispose()

