import asyncio, aiohttp
from client_class_creator import process_orm_model
from orm import linux_db, windows_db


def orm_list_process(orm_list: list, module):
    for orm_model in orm_list:
        process_orm_model(orm_model, module)


async def load_models(module, url: str):
    """request server about orm model data 

    Args:
        module (python module): module where orm models are declared.
        url (str): url 
    """
    models_list = [x for x in dir(module) if "__" not in x]
    async with aiohttp.ClientSession() as session:
        request_body = models_list
        async with session.post(url, json=request_body) as resp:
            data = await resp.json()
        orm_list_process(data, module)


async def load_linux(module):
    """in case we have few different db, on different servers

    Args:
        module (python module): module where orm models are declared. orm models will be changed inside module
    """
    await load_models(module, "http://localhost:8000/models_linux/")


async def load_windows(module):
    """in case we have few different db, on different servers

    Args:
        module (python module): module where orm models are declared. orm models will be changed inside module
    """
    await load_models(module, "http://localhost:8000/models_windows/")


async def main():
    await load_linux(linux_db)
    await load_windows(windows_db)


asyncio.run(main())
