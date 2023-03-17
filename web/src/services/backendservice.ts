import axios from "axios";
import { GameData } from "../types/GameData";

const API_BASE = import.meta.env.VITE_API_BASE;

export const fetchBoard = async (boardId: string) => {
  const resp = await axios.get(`${API_BASE}/board/${boardId}`);
  const data: GameData = resp.data;
  return data;
};

export const makeMove = async (idx: number, boardId: string) => {
  const resp = await axios.post(`${API_BASE}/board/${boardId}`, {
    idx,
  });
  const data: GameData[] = resp.data;
  return data;
};

export const resetBoard = async (boardId: string) => {
  const resp = await axios.delete(`${API_BASE}/board/${boardId}`);
  const data: GameData = resp.data;
  return data;
};

export const createGame = async (size: number, difficulty: number, gamemode: number) => {
  const resp = await axios.post(`${API_BASE}/create`, {
    size,
    difficulty,
    gamemode
  });
  const data: GameData = resp.data;
  return data;
};
