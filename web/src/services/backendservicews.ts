import { WebSocketClient } from "./websocketclient";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";

const API_BASE = import.meta.env.VITE_API_BASE;

//const client = new WebSocketClient(`${API_BASE}/ws`);
const client = new WebSocketClient(`ws://localhost:5173`);
console.log(client)
const connectionID = client.getConnectionId();

export const fetchBoard = async (boardId: string) => {
    const resp = await client.send(connectionID, "fetchBoard", boardId);
    const data: GameData = resp;
    return data;
};

export const makeMove = async (idx: number, boardId: string) => {
    const resp = await client.send(connectionID, "makeMove", idx, boardId);
    const data: GameData[] = resp;
    return data;
};

export const resetBoard = async (boardId: string) => {
    const resp = await client.send(connectionID, "resetBoard", boardId);
    const data: GameData = resp;
};

export const createGame = async (
    size: number,
    difficulty: number,
    gamemode: number
) => {
    const resp = await client.send(connectionID, "createGame", size, difficulty, gamemode);
    const data: GameData = resp.data;
    return data;
};

export const registerUser = async (username: string, password: string) => {
    const resp = await client.send(connectionID, "registerUser", username, password);
    const data: UserData = resp;
    return data;
};

export const loginUser = async (username: string, password: string) => {
    const resp = await client.send(connectionID, "loginUser", username, password);
    const data: UserData = resp;
    return data;
};