import io from "socket.io-client";

const API_BASE = import.meta.env.VITE_API_BASE;

const socket = io(API_BASE);

socket.on("connect", () => {
  console.log(`Connected with session id: ${socket.id}`);
});

export default socket;
