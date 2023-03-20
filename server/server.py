import asyncio
import os

from controller.controller import GameController
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

load_dotenv()
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
    port=os.getenv("PORT") or 3000,
)


@app.get("/board/{board_id}")
async def board(board_id: str):
    if not controller.game_exists(board_id):
        raise HTTPException(404)
    return controller.get_data(board_id)


@app.delete("/board/{board_id}")
async def reset(board_id: str):
    if not controller.game_exists(board_id):
        raise HTTPException(404)
    controller.reset_game(board_id)
    return controller.get_data(board_id)


@app.post("/board/{board_id}")
async def make_move(request: Request, board_id: str):
    if not controller.game_exists(board_id):
        raise HTTPException(404)

    if not controller.players_turn(board_id):
        raise HTTPException(403)

    data = await request.json()
    idx = data["idx"]
    x, y = controller.convert_index_to_xy(board_id, idx)

    print(f"Clicked ({x}, {y})")
    if not controller.is_move_valid(board_id, x, y):
        raise HTTPException(400)

    return controller.send_move(board_id, x, y)


@app.post("/create")
async def create_game(request: Request):
    data = await request.json()
    return controller.new_game(
        data.get("size"), data.get("difficulty"), data.get("gamemode")
    )

@app.post("/register")
async def register_user(request: Request):
    data = await request.json()
    if not controller.user_exists(data.get("username")):
        return controller.register_user(data.get("username"), data.get("password"))
    raise HTTPException(403, "User with that name already exists")


@app.post("/login")
async def login_user(request: Request):
    data = await request.json()
    if controller.user_exists(data.get("username")):
        return controller.login_user(data.get("username"), data.get("password"))
    raise HTTPException(403, "Invalid credentials")


server = Server(config)
asyncio.run(server.serve())
