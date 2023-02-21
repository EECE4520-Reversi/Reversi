import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE

export const fetchBoard = async () => {
    const resp = await axios.get(`${API_BASE}/board/example`);
    return resp.data;
}

export const makeMove = async (idx: number) => {
    console.log(idx)
    const resp = await axios.post(`${API_BASE}/board/example`, {
        idx: idx
    });
    return resp.data;
}

export const resetBoard = async () => {
    const resp = await axios.delete(`${API_BASE}/board/example`);
    return resp.data;
}