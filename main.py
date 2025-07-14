from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
