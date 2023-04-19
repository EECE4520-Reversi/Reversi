import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Board from "./Board";
import socket from "../services/websocket";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";

const Game = ({
  gameData,
  boardID,
  userData,
}: {
  gameData: GameData | undefined;
  boardID: string;
  userData: UserData | undefined;
}) => {
  useEffect(() => {
    socket.emit("updateBoard", boardID);
  }, []);

  return (
    <>
      <div className="grid place-items-center">
        <h1 className="text-8xl text-white-200 font-bold mb-5">Reversi</h1>
        {gameData && (
          <>
            <Board gameData={gameData} userData={userData} />
          </>
        )}
      </div>
    </>
  );
};

export default Game;
