import { useEffect, useState } from "react";
import "./App.css";
import Board from "./components/Board";
import NewGame from "./components/NewGame";
import { createGame, fetchBoard } from "./services/backendservice";
import { useSearchParams } from "react-router-dom";
import { GameData } from "./types/GameData";

function App() {
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
        createGame(8, "Medium").then((gameData) => {
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
    <div className="container">
      <h1 className="text-8xl text-white-200 font-bold mb-5">Reversi</h1>

      {gameData && (
        <>
          <NewGame setGameData={setGameData} />
          <Board gameData={gameData} />
        </>
      )}
    </div>
  );
}

export default App;
