import asyncio
import os

from controller.controller import GameController
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket
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
    port=os.getenv("PORT") or 5173,
)

# list of active connections to front end
active_connections = {}


# entry point for WebSocket connections
@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_handler(websocket)


async def websocket_handler(websocket: WebSocket):
    # Process data and return response
    connection_id = id(websocket)
    active_connections[connection_id] = websocket
    try:
        while True:
            # Receive incoming message from the WebSocket connection
            data = await websocket.receive_json()
            # Decode the function name and arguments from the message
            function_name = data.get("function_name")
            args = data.get("args")
            # Call the appropriate function with the given arguments
            result = await handle_function_call(function_name, *args)
            # Send the result back to the client
            await websocket.send_json({"result": result})
    except:
        # Remove the connection from the dictionary on disconnection
        del active_connections[connection_id]


# Handler function for incoming function calls
async def handle_function_call(function_name: str, *args):
    # Map function names to functions
    function_map = {
        "fetchBoard": fetchBoard_function,
        "makeMove": makeMove_function,
        "resetBoard": resetBoard_function,
        "createGame": createGame_function,
        "registerUser": registerUser_function,
        "loginUser": loginUser_function,
    }
    # Call the appropriate function and return the result
    if function_name in function_map:
        try:
            return await function_map[function_name](*args)
        except Exception as e:
            print("Failed to call function with exception: " + e)
            return None
    else:
        return None


async def fetchBoard_function(board_id: str):
    if not controller.game_exists(board_id):
        raise Exception("Board ${board_id} does not exist")
    return controller.get_board(board_id)


async def makeMove_function(idx: int, board_id: str):
    if not controller.game_exists(board_id):
        raise Exception("Board ${board_id} does not exist")

    if not controller.players_turn(board_id):
        raise Exception("Move received out of turn for board ${board_id}")

    x, y = controller.convert_index_to_xy(idx, board_id)

    print(f"Clicked ({x}, {y})")
    if not controller.is_move_valid(board_id, x, y):
        raise Exception(
            "Invalid move received for board ${board_id} at tile (${x}, ${y})"
        )

    return controller.send_move(board_id, x, y)


async def resetBoard_function(board_id: str):
    if not controller.game_exists(board_id):
        raise Exception("Board ${board_id} does not exist")

    controller.reset_game(board_id)
    return controller.get_data(board_id)


async def createGame_function(size: int, difficulty: int, gamemode: int):
    return controller.new_game(size, difficulty, gamemode)


async def registerUser_function(username: str, password: str):
    if not controller.user_exists(username):
        return controller.register_user(username, password)
    raise Exception("User ${username} already exists")


async def loginUser_function(username: str, password: str):
    if controller.user_exists(username):
        return controller.login_user(username, password)
    raise Exception("Invalid credentials")


# Run the app with uvicorn
server = Server(config)
asyncio.run(server.serve())
