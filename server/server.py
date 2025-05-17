from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_router

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

server.include_router(user_router)


@server.get("/")
async def home():
    return {"message": "remainder app server"}
