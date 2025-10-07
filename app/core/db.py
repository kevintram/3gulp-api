from pydantic import PostgresDsn
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

POSTGRES_URL = PostgresDsn.build(
    scheme="postgresql+asyncpg",
    username="postgres",
    password="postgres",
    host="127.0.0.1",
    port=54322, 
    path="postgres",
)


async def main():
    print(str(POSTGRES_URL))


    engine = create_async_engine(str(POSTGRES_URL), echo=True)

    async with engine.begin() as conn:
        result = await conn.execute(text("select * from topics"))
        print(result.all())

asyncio.run(main())
