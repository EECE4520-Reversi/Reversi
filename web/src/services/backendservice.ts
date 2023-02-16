import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE

export const fetchBoard = async () => {
    const resp = await axios.get(`${API_BASE}/board/example`);
    return resp.data;
}