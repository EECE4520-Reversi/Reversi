import { useEffect, useState } from "react";
import Board from "./Board";
import NewGame from "./NewGame";
import { createGame, fetchBoard } from "../services/backendservice";
import { useSearchParams } from "react-router-dom";
import { GameData } from "../types/GameData";
import { UserData } from "../types/UserData";
import Nav from "./Nav";

const Game = ({userData}: {
  userData: UserData | undefined
})=> {
  const [searchParams, setSearchParams] = useSearchParams();
  const [boardId, setBoardId] = useState<string>(
    new URLSearchParams(searchParams).get("id") || ""
  );
  const [gameData, setGameData] = useState<GameData>();

  useEffect(() => {
    fetchBoard(boardId)
      .then((gameData) => {
        setGameData(gameData);
      })
      .catch(() => {
        createGame(8, 1, 2).then((gameData) => {
          console.log(gameData);
          setBoardId(gameData.id);
          setGameData(gameData);
        });
      });
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
    <div className="grid place-items-center">
      <Nav />
      <h1 className="text-8xl text-white-200 font-bold mb-5">Reversi</h1>
      <h1 className="text-white">{userData?.username}</h1>
      {gameData && (
        <>
          <NewGame setGameData={setGameData} />
          <Board setGameData={setGameData} gameData={gameData} />
        </>
      )}
    </div>
  );
}

export default Game;
