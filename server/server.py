from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Server, Config
import asyncio
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = Config(
    app=app,
    host="0.0.0.0",
    port=4000,
)

@app.get("/board/{board_id}")
async def board(board_id: str):
    return [random.randint(0, 2) for _ in range(12 * 12)]


server = Server(config)
asyncio.run(server.serve())