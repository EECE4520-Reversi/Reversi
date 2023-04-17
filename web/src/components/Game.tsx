import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Board from "./Board";
import socket from "../services/websocket";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";

const Game = ({
  gameData,
  boardID,
}: {
  gameData: GameData | undefined;
  boardID: string;
}) => {
  useEffect(() => {
    socket.emit("updateBoard", boardID);
    console.log(`Refreshing ${boardID}`);
  }, []);

  return (
    <>
      <div className="grid place-items-center">
        <h1 className="text-8xl text-white-200 font-bold mb-5">
          Reversi {boardID}
        </h1>
        {gameData && (
          <>
            <Board gameData={gameData} />
          </>
        )}
      </div>
    </>
  );
};

export default Game;
