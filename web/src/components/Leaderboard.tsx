import { useEffect, useState } from "react";
import { UserData } from "../types/UserData";
import socket from "../services/websocket";

const Leaderboard = () => {
  const [users, setUsers] = useState<UserData[]>([]);

  useEffect(() => {
    socket.on("leaderboard", (data: UserData[]) => {
      setUsers(data);
      console.log(data);
    });

    socket.emit("getLeaderboard");
  }, []);

  return (
    <div>
      <h1 className="text-6xl mb-5">Leaderboard</h1>

      <div className="flex flex-col gap-1 justify-center items-center">
        <div className="w-1/2 grid grid-cols-4">
          <h1 className="text-3xl col-span-3">Username</h1>
          <h1 className="text-3xl">ELO</h1>
        </div>

        {users.map((user) => (
          <div className="bg-black/50 rounded w-1/2 grid grid-cols-4">
            <h1 className="text-3xl col-span-3">{user.username}</h1>
            <h1 className="text-3xl">{user.elo}</h1>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Leaderboard;
