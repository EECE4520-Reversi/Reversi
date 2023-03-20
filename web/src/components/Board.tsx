import { Dispatch, SetStateAction, useEffect, useState } from "react";
import { GamePiece } from "./GamePiece";
import { resetBoard } from "../services/backendservice";
import { GameData } from "../types/GameData";
import Modal from "./Modal";

type Color = { value: string; name: string };
const colors = [
  { value: "bg-green-700", name: "Green" },
  { value: "bg-amber-800", name: "Amber" },
  { value: "bg-[#242424]", name: "Gray" },
  { value: "bg-white", name: "White" },
  { value: "bg-black", name: "Black" },
];

const Board = ({
  gameData,
  setGameData,
}: {
  gameData: GameData;
  setGameData: Dispatch<SetStateAction<GameData | undefined>>;
}) => {
  const [gameOverVisible, setGameOverVisible] = useState<boolean>(false);
  const [settingsVisible, setSettingsVisible] = useState<boolean>(false);
  const [boardColor, setBoardColor] = useState<string>("#18843c");
  const [player1Color, setPlayer1Color] = useState<string>("#ffffff");
  const [player2Color, setPlayer2Color] = useState<string>("#000000");

  console.log(gameData);
  console.log('Game state: ', gameData.state);

  // Sets the new game data, and then refetches
  const updateBoard = async (data: GameData) => {
    setGameData(data);
  };

  const emptyBoard = () => {
    resetBoard(gameData.id).then(setGameData);
  };

  useEffect(() => {
    setGameOverVisible(gameData.state === 3);
  }, [gameData.state]);

  const youWin = <h1 className="text-xl">You Win!</h1>;
  const youlose = <h1 className="text-xl">You Lose!</h1>;

  const settingsComponent = (
    <div className="grid">
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl mr-10">Board Color</h2>
        <input className="my-auto" onChange={(e) => setBoardColor(e.target.value)} type="color" value={boardColor} />
      </div>
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl">Player 1 Color</h2>
        <input className="my-auto" onChange={(e) => setPlayer1Color(e.target.value)} type="color" value={player1Color} />
      </div>
      <div className="mt-3 flex justify-between">
        <h2 className="inline p-2 text-xl">Player 2 Color</h2>
        <input className="my-auto" onChange={(e) => setPlayer2Color(e.target.value)} type="color" value={player2Color} />
      </div>
    </div>
  );

  return (
    <div className="p-3">
      <button
        className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={emptyBoard}
      >
        Reset
      </button>

      <button
        className="ml-2 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
        onClick={() => setSettingsVisible(true)}
      >
        Settings
      </button>



      <div className="flex justify-around mt-5">
        <h3>Your Score: {gameData.score[0]}</h3>
        <h3>Opponent Score: {gameData.score[1]}</h3>
      </div>

      <div className="flex items-center justify-center">
        <div
          className={`grid grid-cols-${gameData.size} grid-rows-${gameData.size}`}
          style={{backgroundColor: `${boardColor}`}}
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
                player1Color={player1Color}
                player2Color={player2Color}
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

      <Modal
        visible={settingsVisible}
        setVisibility={setSettingsVisible}
        title="Settings"
        submitText="Save"
        component={settingsComponent}
      />
    </div>
  );
};

export default Board;
