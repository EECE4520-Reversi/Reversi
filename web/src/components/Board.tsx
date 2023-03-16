import { useEffect, useState } from "react";
import { GamePiece } from "./GamePiece";
import { fetchBoard, resetBoard } from "../services/backendservice";

const Board = ({ gameData }: { gameData: object }) => {
  const [board, setBoard] = useState<number[]>([]);
  const [score, setScore] = useState<number[]>([0, 0]);
  const [size, setSize] = useState<number>(0);
  const [boardId, setBoardId] = useState<string>("");
  const [gameState, setGameState] = useState<number>(0);

  const updateInternalState = (data: any) => {
    console.log(data);
    setBoard(data.board);
    setScore(data.score);
    setBoardId(data.id);
    setSize(data.size);
    setGameState(data.state);
  };

  const updateBoard = () => {
    fetchBoard(boardId).then(updateInternalState);
  };

  const emptyBoard = () => {
    resetBoard(boardId).then(updateInternalState);
  };

  useEffect(() => {
    if (Object.keys(gameData).length) {
      updateInternalState(gameData);
    }
  }, [gameData]);

  return (
    <div className="p-3">
      <button
        className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={emptyBoard}
      >
        Reset
      </button>

      <h3>Your Score: {score[0]}</h3>
      <h3>Opponent Score: {score[1]}</h3>
      <h3>State: {gameState}</h3>

      <div className="flex items-center justify-center">
        <div
          className={`grid grid-cols-${size} grid-rows-${size} bg-green-700`}
        >
          {board &&
            board.map((e, i) => (
              <GamePiece
                key={i}
                idx={i}
                state={e}
                gameState={gameState}
                boardId={boardId}
                updateBoard={updateBoard}
              />
            ))}
        </div>
      </div>
    </div>
  );
};

export default Board;
