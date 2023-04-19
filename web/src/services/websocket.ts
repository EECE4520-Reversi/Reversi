import io from "socket.io-client";

const API_BASE = import.meta.env.VITE_API_BASE;

const socket = io(API_BASE);

export default socket;
