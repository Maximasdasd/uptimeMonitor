import asyncio

from sqlalchemy import text
from uptimemonitor.db.database import engine


async def check_connection() -> None:
    try:
        async with engine.connect() as connection:
            result = await connection.execute(
                text("SELECT current_user, current_database()")
            )
            user, database = result.one()

            print(f"Пользователь: {user}")
            print(f"База данных: {database}")
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(check_connection())