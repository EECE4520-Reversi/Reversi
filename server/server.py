import asyncio
import os

from fastapi_socketio import SocketManager

from controller.controller import GameController
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI()
controller = GameController()
socket_manager = SocketManager(app, cors_allowed_origins="*", mount_location="/")


@socket_manager.on("connect")
async def connect(sid, data):
    print(f"Client connected with session id: {sid}")
    await socket_manager.emit("players", list(controller.online_players.values()))


@socket_manager.on("disconnect")
async def disconnect(sid):
    controller.online_players.pop(sid, None)
    await socket_manager.emit("players", list(controller.online_players.values()))


@socket_manager.on("getBoard")
async def get_board(sid: str, board_id: str):
    if not controller.game_exists(board_id):
        raise HTTPException(404)
    return controller.get_data(board_id)


@socket_manager.on("makeMove")
async def make_move(sid: str, board_id: str, idx: int):
    if not controller.game_exists(board_id):
        raise HTTPException(404)

    if not controller.players_turn(board_id):
        raise HTTPException(403)

    x, y = controller.convert_index_to_xy(board_id, idx)

    print(f"Clicked ({x}, {y})")
    if not controller.is_move_valid(board_id, x, y):
        raise HTTPException(400)

    datas = controller.send_move(board_id, x, y)
    await socket_manager.emit("board", datas[0])

    # The AI delay
    await asyncio.sleep(1)
    await socket_manager.emit("board", datas[1])


@socket_manager.on("resetBoard")
async def reset(sid: str, board_id: str):
    if not controller.game_exists(board_id):
        raise HTTPException(404)
    controller.reset_game(board_id)
    await socket_manager.emit("board", controller.get_data(board_id))


@socket_manager.on("createGame")
async def create_game(sid: str, size: int, difficult: int, gamemode: int):
    data = controller.new_game(size, difficult, gamemode)
    await socket_manager.emit("board", data)


@socket_manager.on("register")
async def register_user(sid: str, username: str, password: str):
    if not controller.user_exists(username):
        data = controller.register_user(sid, username, password)
        if data:
            await socket_manager.emit("players", list(controller.online_players.values()))
            return data
    raise HTTPException(403, "User with that name already exists")


@socket_manager.on("login")
async def login_user(sid: str, username: str, password: str):
    if controller.user_exists(username):
        # If it returns data, logic was successful, emit new player list
        data = controller.login_user(sid, username, password)
        if data:
            await socket_manager.emit("players", list(list(controller.online_players.values())))
            return data

    raise HTTPException(403, "Invalid credentials")

@socket_manager.on("logout")
async def logout_user(sid: str):
    controller.online_players.pop(sid, None)
    await socket_manager.emit("players", list(list(controller.online_players.values())))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
