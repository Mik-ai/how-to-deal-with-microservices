from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from orm.linux_db.router_linux import linux_db_router
from orm.windows_db.router_windows import windows_router

app = FastAPI()


async def get_models(model_names: list[str], router) -> list[dict]:
    """processing orm model before sending

    Args:
        model_names (list[str]): list of requested models 
        router : which router to use

    Returns:
        list[dict]: processed models
    """
    unwanted_fields = {"__dict__", "__doc__", "__module__", "__weakref__"}
    result_list = []
    for orm_name in model_names:
        try:
            ma_dict = dict(vars(router[orm_name]))
            ma_dict = {
                key: value
                for key, value in ma_dict.items()
                if key not in unwanted_fields
            }
            ma_dict["model_name"] = orm_name
            result_list.append(ma_dict)
        except:
            print(orm_name, "not_found")
    return result_list


@app.post("/models_linux/")
async def request_linux_models(model_names: list[str]) -> list[dict]:
    """request models from linux DB

    Args:
        model_names (list[str]): models names

    Returns:
        list[dict]: return structure for each model
    """
    result_list = await get_models(model_names, linux_db_router)
    return result_list


@app.post("/models_windows/")
async def request_windows_models(model_names: list[str]) -> list[dict]:
    """request models from windows DB

    Args:
        model_names (list[str]): models names

    Returns:
        list[dict]: return structure for each model
    """
    result_list = await get_models(model_names, windows_router)
    return result_list


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, loop="asyncio", reload=True)
