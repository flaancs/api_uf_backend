from fastapi import FastAPI
from app.routes import uf_routes

app = FastAPI()
app.include_router(uf_routes.router)
