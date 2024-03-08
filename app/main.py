from fastapi import FastAPI
from app.routes import uf_routes
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "https://api-uf-frontend.vercel.app",
]

app = FastAPI()
app.include_router(uf_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)