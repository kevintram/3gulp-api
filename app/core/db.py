from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
from .config import settings


async def main():
    print(str(settings.POSTGRES_URL))

    engine = create_async_engine(str(settings.POSTGRES_URL), echo=True)

    async with engine.begin() as conn:
        result = await conn.execute(text("select * from topics"))
        print(result.all())

asyncio.run(main())
