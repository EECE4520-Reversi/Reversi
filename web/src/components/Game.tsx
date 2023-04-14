import { useEffect, useState } from "react";
import Board from "./Board";
import NewGame from "./NewGame";
import socket from "../services/websocket";
import { useSearchParams } from "react-router-dom";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";
import Nav from "./Nav";
import { Difficulty, GameType } from "../types/Enums";

const Game = ({
  userData,
  setUserData,
}: {
  userData: UserData | undefined;
  setUserData: (data: UserData | undefined) => void;
}) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [boardId, setBoardId] = useState<string>(
    new URLSearchParams(searchParams).get("id") || ""
  );
  const [gameData, setGameData] = useState<GameData>();

  useEffect(() => {
    socket.emit("getBoard", boardId, (data: GameData) => {
      setGameData(data);
    })

    socket.on("board", (data: GameData) => {
      if (data.id != boardId) return;
      setGameData(data);
    })
  }, []);
  
  useEffect(() => {
    const params = new URLSearchParams();
    params.append("id", boardId);
    setSearchParams(params);
  }, [boardId]);

  useEffect(() => {
    if (gameData && gameData.id !== undefined) setBoardId(gameData.id);
  }, [gameData]);

  return (
    <>
      <div className="grid place-items-center">
        <h1 className="text-8xl text-white-200 font-bold mb-5">Reversi</h1>
        {gameData && (
          <>
            <NewGame setGameData={setGameData} gameData={gameData} />
            <Board setGameData={setGameData} gameData={gameData} />
          </>
        )}
      </div>
    </>
  );
};

export default Game;
