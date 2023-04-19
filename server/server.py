import asyncio
import random

from fastapi_socketio import SocketManager

from controller.controller import GameController
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from model.user import User

load_dotenv()
app = FastAPI()
controller = GameController()
socket_manager = SocketManager(app, cors_allowed_origins="*", mount_location="/")


@socket_manager.on("connect")
async def connect(sid, data):
    print(f"Client connected with session id: {sid}")
    controller.online_players[sid] = f"Guest#{random.randint(0, 10000)}"
    await socket_manager.emit("players", list(controller.online_players.values()))

    user = User(username=controller.online_players[sid])
    await socket_manager.emit("userdata", user.to_dict(), to=sid)


@socket_manager.on("disconnect")
async def disconnect(sid):
    controller.online_players.pop(sid, None)
    await socket_manager.emit("players", list(controller.online_players.values()))


@socket_manager.on("updateBoard")
async def update_board(sid: str, board_id: str):
    if not controller.game_exists(board_id):
        return
    await socket_manager.emit("board", controller.get_data(board_id))


@socket_manager.on("makeMove")
async def make_move(sid: str, board_id: str, idx: int):
    if not controller.game_exists(board_id):
        return

    username = controller.online_players.get(sid)
    if not controller.players_turn(board_id, username):
        return

    x, y = controller.convert_index_to_xy(board_id, idx)

    print(f"Clicked ({x}, {y})")
    if not controller.is_move_valid(board_id, x, y):
        return

    datas = controller.send_move(board_id, x, y)
    await socket_manager.emit("board", datas[0])

    if len(datas) > 1:
        # The AI delay
        await asyncio.sleep(1)
        await socket_manager.emit("board", datas[1])


@socket_manager.on("resetBoard")
async def reset(sid: str, board_id: str):
    if not controller.game_exists(board_id):
        return
    controller.reset_game(board_id)
    await socket_manager.emit("board", controller.get_data(board_id))


@socket_manager.on("createGame")
async def create_game(sid: str, size: int, difficult: int, gamemode: int):
    username = controller.online_players.get(sid)
    board_id = controller.new_game(size, difficult, gamemode, [username])
    await socket_manager.emit("openGames", controller.joinable_games())
    return board_id


@socket_manager.on("joinGame")
async def join_game(sid: str, board_id: str):
    username = controller.online_players.get(sid)
    controller.add_player(board_id, username)
    await socket_manager.emit("openGames", controller.joinable_games())
    await socket_manager.emit("board", controller.get_data(board_id))


@socket_manager.on("register")
async def register_user(sid: str, username: str, password: str):
    if not controller.user_exists(username):
        data = controller.register_user(sid, username, password)
        await socket_manager.emit("players", list(controller.online_players.values()))
        await socket_manager.emit("userdata", data, to=sid)
        return

    # TODO: Show error message in UI, we cant use exceptions
    raise HTTPException(403, "User with that name already exists")


@socket_manager.on("login")
async def login_user(sid: str, username: str, password: str):
    if controller.user_exists(username):
        # If it returns data, logic was successful, emit new player list
        data = controller.login_user(sid, username, password)
        if data:
            await socket_manager.emit(
                "players", list(list(controller.online_players.values()))
            )
            await socket_manager.emit("userdata", data, to=sid)
            return

    # TODO: Show error message in UI, we cant use exceptions
    raise HTTPException(403, "Invalid credentials")


@socket_manager.on("logout")
async def logout_user(sid: str):
    controller.online_players.pop(sid, None)
    await socket_manager.emit("players", list(list(controller.online_players.values())))


@socket_manager.on("joinableGames")
async def joinable_games(sid: str):
    return controller.joinable_games()


@socket_manager.on("getLeaderboard")
async def get_leaderboard(sid: str):
    data = [User.from_dict(data).to_dict() for data in controller.get_leaderboard()]
    await socket_manager.emit("leaderboard", data, to=sid)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
