import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE

export const fetchBoard = async (boardId: string) => {
    const resp = await axios.get(`${API_BASE}/board/${boardId}`);
    return resp.data;
}

export const makeMove = async (idx: number, boardId: string) => {
    console.log(idx)
    const resp = await axios.post(`${API_BASE}/board/${boardId}`, {
        idx: idx
    });
    return resp.data;
}

export const resetBoard = async (boardId: string) => {
    const resp = await axios.delete(`${API_BASE}/board/${boardId}`);
    return resp.data;
}