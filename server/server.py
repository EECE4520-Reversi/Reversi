import asyncio

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from controller.controller import GameController

app = FastAPI()
controller = GameController()

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
    return controller.get_data(board_id)


@app.delete("/board/{board_id}")
async def reset(board_id: str):
    controller.reset_game(board_id)
    return controller.get_data(board_id)


@app.post("/board/{board_id}")
async def make_move(request: Request, board_id: str):
    data = await request.json()
    idx = data["idx"]
    x, y = idx % 8, idx // 8
    print(f"Clicked ({x}, {y})")
    return controller.send_move(board_id, x, y)


server = Server(config)
asyncio.run(server.serve())
