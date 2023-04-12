import { WebSocketClient } from "./websocketclient";

const API_BASE = import.meta.env.VITE_API_BASE;

const client = new WebSocketClient(`${API_BASE}/ws`);
const connectionID = client.getConnectionId();

export const fetchBoard = async (boardId: string) => {
    const resp = await client.send(connectionID, "fetchBoard", boardId);
};

export const makeMove = async (idx: number, boardId: string) => {
    const resp = await client.send(connectionID, "makeMove", idx, boardId);
};

export const resetBoard = async (boardId: string) => {
    const resp = await client.send(connectionID, "resetBoard", boardId);
};

export const createGame = async (
    size: number,
    difficulty: number,
    gamemode: number
) => {
    const resp = await client.send(connectionID, "createGame", size, difficulty, gamemode);
};

export const registerUser = async (username: string, password: string) => {
    const resp = await client.send(connectionID, "registerUser", username, password);
};

export const loginUser = async (username: string, password: string) => {
    const resp = await client.send(connectionID, "loginUser", username, password);
};