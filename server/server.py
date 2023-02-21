from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Server, Config
import asyncio
import random
from model import Game
from controller import Controller
from fastapi import Request

app = FastAPI()
game = Game()
controller = Controller(game)

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
    return controller.get_board()

@app.post("/board/{board_id}")
async def board(request: Request, board_id: str):
    data = await request.json()
    idx = data["idx"]
    x, y = idx % 12, idx // 12
    print(f"Clicked ({x}, {y})")
    return controller.send_move(x, y)



server = Server(config)

asyncio.run(server.serve())