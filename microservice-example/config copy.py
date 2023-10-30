from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import time
import asyncio
import functools


OZON_BASE_URL = "https://api-seller.ozon.ru"
TESSERACT_PATH = r"D:\Program Files\tesseractOCR\tesseract.exe"


DB_LOGIN = ""
DB_PASSWORD = ""
DB_IP = ""
DB_NAME = ""


def retry_async(num_attempts):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for try_index in range(num_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(
                        f"Exception occurred: {e}. Retrying... ({try_index}/{num_attempts})"
                    )
                    await asyncio.sleep(1)
            else:
                print(f"Failed after {num_attempts} attempts.")

        return wrapper

    return decorator


def do_retry_on_fail(func):
    def wrapper(*args, **kwargs):
        reconnct_tries = 5
        for try_index in range(reconnct_tries):
            try:
                print(try_index, reconnct_tries)
                return func(*args, **kwargs)
            except:
                print(f"Unable to execute: {func.__name__}")
                time.sleep(1)

    return wrapper


engine = create_engine(
    f"postgresql+psycopg2://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
)

engine_async = create_async_engine(
    f"postgresql+asyncpg://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
)
