import uvicorn

from fastapi import FastAPI
from config import *
from logger.log import new_logger
from routers import example

# 开启一个logger
logger = new_logger("__init__")

openapi_url = os.environ.get("JACARANDA_API_OPENAPI", None)
if debug and openapi_url is None:
    openapi_url = "/openapi.json"
    logger.warning("JACARANDA_API_OPENAPI is not set, using default value: %s", openapi_url)

docs_url = os.environ.get("JACARANDA_API_DOCS", None)
if debug and docs_url is None:
    docs_url = "/docs"
    logger.warning("JACARANDA_API_DOCS is not set, using default value: %s", docs_url)

redoc_url = os.environ.get("JACARANDA_API_REDOC", None)
if debug and redoc_url is None:
    redoc_url = "/redoc"
    logger.warning("JACARANDA_API_REDOC is not set, using default value: %s", redoc_url)

host = os.environ.get("UVICORN_HOST", None)
if debug and host is None:
    host = "localhost"
    logger.warning("UVICORN_HOST is not set, using default value: %s", host)

port = os.environ.get("UVICORN_PORT", None)
if debug and port is None:
    port = 8000
    logger.warning("UVICORN_PORT is not set, using default value: %s", port)

if debug:
    # 开启开启 uvicorn debug模式
    os.environ["PYTHONBREAKPOINT"] = "pdb.set_trace"

# 默认开启reload
reload = bool(int(os.environ.get("UVICORN_RELOAD", 1)))

app = FastAPI(openapi_url=openapi_url, docs_url=docs_url, redoc_url=redoc_url)

"""
def register_routers(application: FastAPI, routers_dir: str = "routers"):
    # Iterate through the routers directory
    for file_name in os.listdir(routers_dir):
        # Only process .py files
        if file_name.endswith(".py") and not file_name.startswith("__"):
            module_name = file_name[:-3]  # Remove .py extension
            module_path = f"{routers_dir}.{module_name}"
            # Import the router module
            router_module = importlib.import_module(module_path)
            logger.debug("Successfully imported router module: %s", module_path)
            if hasattr(router_module, "router"):
                app.include_router(router_module.router)
                logger.debug("Successfully registered router: %s", module_path)

register_routers(app)
"""

app.include_router(example.router)

@app.get("/")
async def root():
    return {"message": f"Welcome to Jacarandastock"}


if __name__ == '__main__':
    uvicorn.run("main:app", host=host, port=port, reload=reload)
