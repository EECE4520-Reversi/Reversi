import { Dispatch, SetStateAction, useEffect, useState } from "react";
import Board from "./Board";
import socket from "../services/websocket";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";

const Game = ({
  gameData,
  boardID,
<<<<<<< HEAD
  userData,
}: {
  gameData: GameData | undefined;
  boardID: string;
  userData: UserData | undefined;
=======
}: {
  gameData: GameData | undefined;
  boardID: string;
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
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
<<<<<<< HEAD
            <Board gameData={gameData} userData={userData} />
=======
            <Board gameData={gameData} />
>>>>>>> 40bf264c4db7b2710872012bc1f659e17a41fd14
          </>
        )}
      </div>
    </>
  );
};

export default Game;
