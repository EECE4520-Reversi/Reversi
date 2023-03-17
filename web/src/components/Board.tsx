import { Dispatch, SetStateAction, useEffect, useState } from "react";
import { GamePiece } from "./GamePiece";
import { fetchBoard, resetBoard } from "../services/backendservice";
import { GameData } from "../types/GameData";
import Modal from "./Modal";

const Board = ({ gameData, setGameData }: { 
  gameData: GameData,
  setGameData: Dispatch<SetStateAction<GameData | undefined>>
 }) => {
  const [gameOverVisible, setGameOverVisible] = useState<boolean>(false);



  // Sets the new game data, and then refetches
  const updateBoard = async (data: GameData) => {
    setGameData(data);
    await delay(2000);
    setGameData(await fetchBoard(data.id));
  };

  const emptyBoard = () => {
    resetBoard(gameData.id).then(setGameData);
  };

  useEffect(() => {
    setGameOverVisible(gameData.state === 3);
  }, [gameData.state])

  const youWin = <h1 className="text-xl">You Win!</h1>
  const youlose = <h1 className="text-xl">You Lose!</h1>

  return (
    <div className="p-3">
      <button
        className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={emptyBoard}
      >
        Reset
      </button>

      <h3>Your Score: {gameData.score[0]}</h3>
      <h3>Opponent Score: {gameData.score[1]}</h3>
      <h3>State: {gameData.state}</h3>

      <div className="flex items-center justify-center">
        <div
          className={`grid grid-cols-${gameData.size} grid-rows-${gameData.size} bg-green-700`}
        >
          {gameData.board &&
            gameData.board.map((e, i) => (
              <GamePiece
                key={i}
                idx={i}
                state={e}
                gameState={gameData.state}
                boardId={gameData.id}
                updateBoard={updateBoard}
              />
            ))}
        </div>
      </div>

      <Modal
          visible={gameOverVisible}
          setVisibility={setGameOverVisible}
          title="Game Over"
          submitText="Create"
          component={gameData.score[0] > gameData.score[1] ? youWin : youlose}
        />
        
    </div>
  );
};

export default Board;
