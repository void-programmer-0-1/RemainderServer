from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI(
    title="Remainder App",
    description="Events and Task remainder server for you"
)

server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@server.get("/")
async def home():
    return {"message": "memory server"}
